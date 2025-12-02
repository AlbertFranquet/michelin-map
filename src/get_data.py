# src/load_data.py

import pandas as pd
import os

RAW_CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "data", "raw", "michelin_my_maps.csv")

def load_data(path=RAW_CSV_PATH):
    df = pd.read_csv(path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Filter only starred restaurants (ignore Bib Gourmand, Selected, etc.)
    # df = df[df["Award"].isin(["1 Star", "2 Stars", "3 Stars"])].copy()

    # Convert award to integer stars
    def award_to_int(a):
        if a == "1 Star":
            return 1
        elif a == "2 Stars":
            return 2
        elif a == "3 Stars":
            return 3
        else:
            return 0

    df["stars"] = df["Award"].apply(award_to_int)

    # If there"s a green star flag — include it; else default False
    if "GreenStar" in df.columns:
        df["green_star"] = df["GreenStar"].astype(bool)
    else:
        df["green_star"] = False

    # Drop rows with missing coordinates
    df = df.dropna(subset=["Latitude", "Longitude"])

    # Convert Location to City and Country
    def get_city(l):
        l_array = l.split(",")
        return l_array[0]
    def get_country(l):
        l_array = l.split(",")
        return l_array[-1]
    
    df["City"] = df["Location"].apply(get_city)
    df["Country"] = df["Location"].apply(get_country)

    # Clean PhoneNumber column
    if "PhoneNumber" in df.columns:
        df["PhoneNumber"] = df["PhoneNumber"].fillna("").astype(str).str.strip()
    else:
        df["PhoneNumber"] = ""
    df["PhoneNumber"] = df["PhoneNumber"].apply(lambda x: x.removesuffix(".0") if x.endswith(".0") else x)

    # Clean WebsiteUrl column
    if "WebsiteUrl" in df.columns:
        df["WebsiteUrl"] = df["WebsiteUrl"].fillna("").astype(str).str.strip()
    else:
        df["WebsiteUrl"] = ""

    return df

if __name__ == "__main__":
    df = load_data()
    df_clean = clean_data(df)
    print(f"Total starred restaurants: {len(df_clean)}")
    print(df_clean[["Name", "City", "Country", "Latitude", "Longitude","stars","green_star"]].head())
