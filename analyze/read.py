import pandas as pd

def histdata(infile):
    # read, rename columns, parse datetime
    columns = ["DateTime", "Open", "High", "Low", "Close"] # skip  "Volume"
    df = pd.read_csv(infile, sep=";",
                     header=None, names=columns, usecols=[0, 1,2,3,4],
                     index_col=0, parse_dates=True)

    return df
