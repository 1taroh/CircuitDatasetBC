
from pathlib import Path
import pandas as pd
from dataset import search, dataset_df

result = search(
    dataset_df,
    boundary_type="match",
    graph_type="Branch",
    p_G_load=0.1,
    p_L=0.0,
    p_C=0.0,
    missing_values=5,
)
raw_data = Path(result["path_raw"].iloc[0])
processed_data = Path(result["path_processed"].iloc[0])

df_raw = pd.read_csv(raw_data)
df_processed = pd.read_csv(processed_data)
print(df_raw.head())
print(df_processed.head())
