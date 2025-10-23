#!/usr/bin/env python3

from os import sep
import pandas as pd

def main():
    data =pd.read_csv("src\municipal.tsv", sep="\t")
    print(f"Shape: {data.shape[0]},{data.shape[1]}")
    print("Columns:")
    names = data.columns
    for name in names:
        print(name)
    


if __name__ == "__main__":
    main()
