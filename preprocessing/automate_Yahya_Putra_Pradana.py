"""Reusable cleaning for the ISLR simulated credit-default data."""
from pathlib import Path
import pandas as pd

TARGET = "default"
FEATURES = ["student", "balance", "income"]

def load_and_clean(input_path):
    df = pd.read_csv(input_path)
    required = {"default", "student", "balance", "income"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.drop(columns=[c for c in ["rownames", "Unnamed: 0"] if c in df.columns])
    df = df.drop_duplicates().copy()
    df["default"] = df["default"].map({"No": 0, "Yes": 1})
    df["student"] = df["student"].astype(str).str.strip().str.lower()
    for col in ["balance", "income"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=FEATURES + [TARGET]).reset_index(drop=True)
    if not set(df[TARGET].unique()).issubset({0, 1}):
        raise ValueError("Target must be binary 0/1")
    return df

def preprocess_file(input_path, output_path):
    clean = load_and_clean(input_path)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(output_path, index=False)
    return clean

if __name__ == "__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--input", default="../credit_default_raw.csv")
    p.add_argument("--output", default="../credit_default_preprocessed.csv")
    a=p.parse_args(); df=preprocess_file(a.input,a.output)
    print(f"Saved {len(df)} rows; default rate={df.default.mean():.4%}; output={a.output}")
