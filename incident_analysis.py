import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def calculate_total_incidents(df):
    df["Total_Incidents"] = df["Fatal_Accidents"] + df["Serious_Incidents"]
    return df

def calculate_conditional_probabilities(df):
    total = df["Total_Incidents"].sum()
    df["Incident_Probability"] = df["Total_Incidents"] / total
    return df.sort_values(by="Incident_Probability", ascending=False)

if __name__ == "__main__":
    df = load_data("data/airline_incident_data.csv")
    df = calculate_total_incidents(df)
    df = calculate_conditional_probabilities(df)
    print(df[["Airline", "Total_Incidents", "Incident_Probability"]])

