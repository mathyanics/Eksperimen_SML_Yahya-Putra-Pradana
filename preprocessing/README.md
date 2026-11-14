# Preprocessing

`automate_Yahya_Putra_Pradana.py` removes the row identifier, removes duplicate rows, encodes `default` as 0/1, normalizes the `student` category, parses numeric fields, and drops rows missing required fields. It does not fit transformations on the full dataset; scaling/encoding are fitted inside the train-only model pipeline.

Run: `python automate_Yahya_Putra_Pradana.py --input ../credit_default_raw.csv --output ../credit_default_preprocessed.csv`
