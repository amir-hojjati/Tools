import csv
import re

import pandas as pd


def search_csv(keyword, data):
    pattern = re.compile(keyword)
    results = []
    for i, row in data.iterrows():
        for field in row:
            if pattern.search(str(field)):
                results.append(row)
                break
    return pd.DataFrame(results)
