from kafka import KafkaConsumer
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from json import loads
from datetime import datetime
import pickle

# get current date
current_date = datetime.now().strftime("%Y-%m-%d")


DB_URL = "postgresql://postgres:postgres@localhost:5432/breast_cancer_db"
TABLE_NAME_RAW_DATA = "breast_cancer_raw_data"
TABLE_NAME_MODEL_OUTPUT = "breast_cancer_model_output"


def connect_to_db():
    """
    Connects to the database using the provided DB_URL.

    Returns:
        connection (Connection): A connection object to the database.
            Returns None if an error occurs while connecting to the database.
    """
    try:
        engine = create_engine(DB_URL)
        return engine.connect()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


# define a consumer that waits for new messages
def kafka_python_consumer():
    """
    Consumes messages from a Kafka topic and performs the following actions:

    1. Connects to a database using the provided DB_URL.
    2. Appends the received message value to a list.
    3. Prints the received message value.
    4. Commits the consumer offset.
    5. Inserts the message value into a database table.
    6. Generates a dataframe from the first message value.
    7. Extracts the "id" column from the dataframe and removes it.
    8. Loads a KNN model from a pickle file.
    9. Predicts the diagnosis and probability using the KNN model on the dataframe.
    10. Creates a dataframe with the "id", "diagnosis", and "probability" columns.
    11. Writes the prediction dataframe to a database table.

    Parameters:
        None

    Returns:
        None
    """

    # Consumer using the topic name and setting a group id
    consumer = KafkaConsumer(
        "breast-cancer-streaming",
        group_id="breast-cancer-group",
        bootstrap_servers="localhost:9093",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )
    for msg in consumer:

        for data in msg.value:
            print(f"Received message: {data}")
            consumer.commit()
            conn = connect_to_db()

            columns = ", ".join((data.keys()))
            values = ", ".join([str(value) for value in data.values()])
            insert_sql = (
                f"""INSERT INTO {TABLE_NAME_RAW_DATA} (%s, time) VALUES (%s, CURRENT_DATE);"""
                % (
                    columns,
                    values,
                )
            )

            conn.execute(text(insert_sql))
            conn.commit()

            # Generate dataframe from data dict
            df = pd.DataFrame.from_dict(data, orient="index").T
            print(df)

            # Extract id from dataframe to push to database, and remove id from dataframe to make prediction
            id = df["id"]
            df = df.drop(["id"], axis=1)

            # Load model
            knn = pickle.load(open("knn_model.pkl", "rb"))

            # Make prediction
            prediction = knn.predict(df)
            probability = knn.predict_proba(df)
            max_proba = probability.max(axis=1)

            # Create prediction dataframe
            prediction_dataframe = pd.DataFrame(
                {"id": id, "diagnosis": prediction, "probability": max_proba}
            )

            # Wirte prediction to db using pandas, append value to table
            prediction_dataframe.to_sql(
                name=TABLE_NAME_MODEL_OUTPUT, con=conn, if_exists="append", index=False
            )

        print("Waiting for next message...")


print("start consuming")

# start the consumer
kafka_python_consumer()
