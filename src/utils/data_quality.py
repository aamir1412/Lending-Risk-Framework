# src/utils/data_quality

def drop_critical_nulls(df, subset_cols):
    """Drops rows with NULLs in specified columns."""
    return df.dropna(subset=subset_cols)