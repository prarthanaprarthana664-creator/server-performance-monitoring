import pandas as pd

def load_data(file_path):
   metadata = pd.read_excel(file_path, sheet_name="Server_Metadata", engine="openpyxl")
   station1 = pd.read_excel(file_path, sheet_name="Server_Performance_Station1", engine="openpyxl")
   station2 = pd.read_excel(file_path, sheet_name="Server_Performance_Station2", engine="openpyxl")
   return metadata, station1, station2


def clean_data(df):
    # remove unwanted columns
    df = df.drop(columns=["Config_Version", "Deployment_Token"], errors='ignore')

    # fill missing values
    df = df.fillna(method='ffill')

    return df


def transform_data(metadata, s1, s2):
    s1 = clean_data(s1)
    s2 = clean_data(s2)

    combined_data = pd.concat([s1, s2])

    # merge with metadata
    final_data = combined_data.merge(metadata, on="Server_ID", how="left")

    return final_data