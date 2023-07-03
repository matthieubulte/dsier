if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    tickers_df = pd.read_csv('../data/indices.csv')
    df = pd.read_csv('../data/raw_data.csv')

    # Remove days with NAs and log how many are missing
    is_na = df.isna().any(axis=1)
    print(f"Found {is_na.sum()} NA rows out of {df.shape[0]}. Removing them.")
    df = df[~is_na]

    # Create for each month a correlation matrix between the different indices
    df['year-month'] = pd.to_datetime(df.Date).dt.strftime('%Y-%m')
    indices = tickers_df.ticker.unique()
    corr_df = df.groupby('year-month').apply(lambda sdf: np.corrcoef(sdf[indices].values.T))
    corr_mats = np.r_[corr_df.values.tolist()] # T x n_indices x n_indices

    # Save the resulting matrix time series
    np.save("../data/matrices_ts.npy", corr_mats)