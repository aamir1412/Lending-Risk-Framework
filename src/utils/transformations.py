def standardize_column_names(df, rename_map, strict=False):
    """
    Renames columns using a dictionary.
    If strict=True, fails immediately if a source column is missing.
    """
    if strict:
        missing_cols = [col for col in rename_map.keys() if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Schema mismatch. Missing columns to rename: {missing_cols}")
            
    # Native PySpark 3.4+ dictionary rename
    return df.withColumnsRenamed(rename_map)