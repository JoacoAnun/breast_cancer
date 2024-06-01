from kafka import KafkaProducer


def produce_kafka_string(json_as_string):
    # Create producer
    producer = KafkaProducer(bootstrap_servers="localhost:9093", acks=1)
    producer.send("breast-cancer-streaming", bytes(json_as_string, "utf-8"))
    producer.flush()


if __name__ == "__main__":
    # Generate random sample
    import pandas as pd
    import numpy as np

    # Create a DataFrame with 30 columns
    num_columns = 31
    data = pd.DataFrame(
        np.random.uniform(1, 100, size=(1, num_columns)),
        columns=[
            "id",
            "radius_mean",
            "texture_mean",
            "perimeter_mean",
            "area_mean",
            "smoothness_mean",
            "compactness_mean",
            "concavity_mean",
            "concave_points_mean",
            "symmetry_mean",
            "fractal_dimension_mean",
            "radius_se",
            "texture_se",
            "perimeter_se",
            "area_se",
            "smoothness_se",
            "compactness_se",
            "concavity_se",
            "concave_points_se",
            "symmetry_se",
            "fractal_dimension_se",
            "radius_worst",
            "texture_worst",
            "perimeter_worst",
            "area_worst",
            "smoothness_worst",
            "compactness_worst",
            "concavity_worst",
            "concave_points_worst",
            "symmetry_worst",
            "fractal_dimension_worst",
        ],
    )
    print(data)

    # Convert DataFrame to JSON
    sample_json_as_string = data.to_json(orient="records")
    print(sample_json_as_string)
    produce_kafka_string(sample_json_as_string)
