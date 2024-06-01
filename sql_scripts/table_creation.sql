-- Create table to store raw data
CREATE TABLE breast_cancer_raw_data (
    id INT PRIMARY KEY,
    radius_mean FLOAT,
    texture_mean FLOAT,
    perimeter_mean FLOAT,
    area_mean FLOAT,
    smoothness_mean FLOAT,
    compactness_mean FLOAT,
    concavity_mean FLOAT,
    concave_points_mean FLOAT,
    symmetry_mean FLOAT,
    fractal_dimension_mean FLOAT,
    radius_se FLOAT,
    texture_se FLOAT,
    perimeter_se FLOAT,
    area_se FLOAT,
    smoothness_se FLOAT,
    compactness_se FLOAT,
    concavity_se FLOAT,
    concave_points_se FLOAT,
    symmetry_se FLOAT,
    fractal_dimension_se FLOAT,
    radius_worst FLOAT,
    texture_worst FLOAT,
    perimeter_worst FLOAT,
    area_worst FLOAT,
    smoothness_worst FLOAT,
    compactness_worst FLOAT,
    concavity_worst FLOAT,
    concave_points_worst FLOAT,
    symmetry_worst FLOAT,
    fractal_dimension_worst FLOAT,
    date_value DATE
);

-- Create table to store model output
CREATE TABLE breast_cancer_model_output (
    id INT PRIMARY KEY,
    diagnosis VARCHAR(1),
    probability FLOAT
);


-- Create table to store training data
CREATE TABLE breast_cancer_training_data (
    id INT PRIMARY KEY,
    diagnosis VARCHAR(1),
    radius_mean FLOAT,
    texture_mean FLOAT,
    perimeter_mean FLOAT,
    area_mean FLOAT,
    smoothness_mean FLOAT,
    compactness_mean FLOAT,
    concavity_mean FLOAT,
    concave_points_mean FLOAT,
    symmetry_mean FLOAT,
    fractal_dimension_mean FLOAT,
    radius_se FLOAT,
    texture_se FLOAT,
    perimeter_se FLOAT,
    area_se FLOAT,
    smoothness_se FLOAT,
    compactness_se FLOAT,
    concavity_se FLOAT,
    concave_points_se FLOAT,
    symmetry_se FLOAT,
    fractal_dimension_se FLOAT,
    radius_worst FLOAT,
    texture_worst FLOAT,
    perimeter_worst FLOAT,
    area_worst FLOAT,
    smoothness_worst FLOAT,
    compactness_worst FLOAT,
    concavity_worst FLOAT,
    concave_points_worst FLOAT,
    symmetry_worst FLOAT,
    fractal_dimension_worst FLOAT,
    date_value DATE
);

-- Create table to store processed data
CREATE TABLE breast_cancer_processed_data (
    id INT PRIMARY KEY,
    diagnosis VARCHAR(1),
    radius_mean FLOAT,
    texture_mean FLOAT,
    perimeter_mean FLOAT,
    area_mean FLOAT,
    smoothness_mean FLOAT,
    compactness_mean FLOAT,
    concavity_mean FLOAT,
    concave_points_mean FLOAT,
    symmetry_mean FLOAT,
    fractal_dimension_mean FLOAT,
    radius_se FLOAT,
    texture_se FLOAT,
    perimeter_se FLOAT,
    area_se FLOAT,
    smoothness_se FLOAT,
    compactness_se FLOAT,
    concavity_se FLOAT,
    concave_points_se FLOAT,
    symmetry_se FLOAT,
    fractal_dimension_se FLOAT,
    radius_worst FLOAT,
    texture_worst FLOAT,
    perimeter_worst FLOAT,
    area_worst FLOAT,
    smoothness_worst FLOAT,
    compactness_worst FLOAT,
    concavity_worst FLOAT,
    concave_points_worst FLOAT,
    symmetry_worst FLOAT,
    fractal_dimension_worst FLOAT
);



-- Create a stored procedure to get a row from the raw data table, given an id combine it with the model output table and stored in a new table called breast_cancer_processed_data
CREATE PROCEDURE breast_cancer_cross_data(patient_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO breast_cancer_processed_data
    SELECT
        breast_cancer_raw_data.id,
        breast_cancer_raw_data.radius_mean,
        breast_cancer_raw_data.texture_mean,
        breast_cancer_raw_data.perimeter_mean,
        breast_cancer_raw_data.area_mean,
        breast_cancer_raw_data.smoothness_mean,
        breast_cancer_raw_data.compactness_mean,
        breast_cancer_raw_data.concavity_mean,
        breast_cancer_raw_data.concave_points_mean,
        breast_cancer_raw_data.symmetry_mean,
        breast_cancer_raw_data.fractal_dimension_mean,
        breast_cancer_raw_data.radius_se,
        breast_cancer_raw_data.texture_se,
        breast_cancer_raw_data.perimeter_se,
        breast_cancer_raw_data.area_se,
        breast_cancer_raw_data.smoothness_se,
        breast_cancer_raw_data.compactness_se,
        breast_cancer_raw_data.concavity_se,
        breast_cancer_raw_data.concave_points_se,
        breast_cancer_raw_data.symmetry_se,
        breast_cancer_raw_data.fractal_dimension_se,
        breast_cancer_raw_data.radius_worst,
        breast_cancer_raw_data.texture_worst,
        breast_cancer_raw_data.perimeter_worst,
        breast_cancer_raw_data.area_worst,
        breast_cancer_raw_data.smoothness_worst,
        breast_cancer_raw_data.compactness_worst,
        breast_cancer_raw_data.concavity_worst,
        breast_cancer_raw_data.concave_points_worst,
        breast_cancer_raw_data.symmetry_worst,
        breast_cancer_raw_data.fractal_dimension_worst,
        breast_cancer_raw_data.date_value,
        breast_cancer_model_output.diagnosis,
        breast_cancer_model_output.probability
    FROM breast_cancer_raw_data
    JOIN breast_cancer_model_output
    ON breast_cancer_raw_data.id = breast_cancer_model_output.id;
END;
$$;
