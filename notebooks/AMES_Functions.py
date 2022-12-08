def pth_percentile_na(data, pct = 10):
    df = data
    thresh = df.isnull().sum().\
    quantile([(100-pct)/100 for x in range(100-pct,100)])\
    .values[0]
    return [f'{col}: {df[col].isnull().sum()}' for col in df.columns if df[col].\
     isnull().sum() > thresh]

def impute(data, feature, imp='None'):
    data[data[feature].isna()] = imp
    return data