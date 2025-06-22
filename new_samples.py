import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer as Synthesizer
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import get_column_plot, get_column_pair_plot

from sdv.datasets.local import load_csvs


# Step 1: Load the dataset
df = pd.read_csv("dataset.csv", sep=';')



# Step 2: Detect metadata
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=df)

# Optional: Save metadata
metadata.save_to_json("metadata.json",mode="overwrite")


# Step 3: Train model
model = Synthesizer(metadata=metadata)
model.fit(df)

# Step 4: Generate synthetic data
synthetic_data = model.sample(num_rows=500)

print(synthetic_data.head())

# Step 5: Save synthetic data to CSV
synthetic_data.to_csv("synthetic_dataset.csv", index=False, sep=';')



# Step 6: Evaluate quality of synthetic data
from sdv.evaluation.single_table import evaluate_quality

quality_report = evaluate_quality(
    df,
    synthetic_data,
    metadata)



    


