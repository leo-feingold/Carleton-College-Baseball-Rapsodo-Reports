import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, "r") as f:
        first_line = f.readline() # CSV has a break in the first line so it is blank. 
        player_id = f.readline().strip().split(",")[1]
        player_name = f.readline().strip().split(",")[1]

 

    df = pd.read_csv(file_path, skiprows = 4) # Actual data starts here
    df["Player ID"] = player_id
    df["Player Name"] = player_name

    return df


def main():
    df = load_data("/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/Ananth_Data/940780_pitching_b3f83e223b9bb1197284.csv")
    print(df.columns)




if __name__ == "__main__":
        main()
