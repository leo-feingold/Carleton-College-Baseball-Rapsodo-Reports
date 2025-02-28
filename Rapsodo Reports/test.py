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

def date(df):
    print(df.Date)

def rollingFastballVelo(df):

    df_fastball = df.loc[df["Pitch Type"] == "Fastball"]
    df_fastball = df_fastball.sort_values(by="Date", ascending=True)
    print(len(df_fastball))
    df_fastball["Rolling Velo"] = df_fastball["Velocity"].rolling(window=10).mean()


    plt.figure(figsize=(10,5))
    plt.plot(df_fastball["Date"], df_fastball["Rolling Velo"], marker="o", linestyle="-", label="Rolling 10-Pitch Fastball Velo")
    plt.xlabel("Date")
    plt.ylabel("Velocity (mph)")
    plt.title("Rolling 10-Pitch Average Velocity (Fastballs)")
    plt.legend()
    plt.grid(True)
    num_ticks = 5  # Adjust the number of ticks shown
    plt.xticks(df_fastball["Date"][::len(df_fastball)//num_ticks], rotation=20)
    plt.show()


def main():
    df = load_data("/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/Ananth_Data/940780_pitching_8328afd9242cc19906c4.csv")
    rollingFastballVelo(df)
    #date(df)



if __name__ == "__main__":
        main()
