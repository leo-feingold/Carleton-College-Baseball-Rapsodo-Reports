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

def helper_get_columns(df):
    '''
        ['No', 'Date', 'Pitch ID', 'Pitch Type', 'Is Strike', 'Strike Zone Side',
       'Strike Zone Height', 'Velocity', 'Total Spin', 'True Spin (release)',
       'Spin Efficiency (release)', 'Spin Direction', 'Spin Confidence',
       'VB (trajectory)', 'HB (trajectory)', 'SSW VB', 'SSW HB', 'VB (spin)',
       'HB (spin)', 'Horizontal Angle', 'Release Angle', 'Release Height',
       'Release Side', 'Release Extension (ft)', 'Gyro Degree (deg)',
       'Unique ID', 'Device Serial Number', 'SO - latLongConfidence',
       'SO - latitude', 'SO - longitude', 'SO - rotMatConfidence',
       'SO - timestamp', 'SO - Xx', 'SO - Xy', 'SO - Xz', 'SO - Yx', 'SO - Yy',
       'SO - Yz', 'SO - Zx', 'SO - Zy', 'SO - Zz', 'Horizontal Approach Angle',
       'Vertical Approach Angle', 'Session Name', 'Intent Type', 'Player ID',
       'Player Name']
    '''

def rollingFastballVelo(df):

    df_fastball = df.loc[df["Pitch Type"] == "Fastball"]
    df_fastball["Date"] = pd.to_datetime(df_fastball["Date"], errors="coerce")
    df_fastball = df_fastball.sort_values(by="No", ascending=False)
    df_fastball["Rolling Velo"] = df_fastball["Velocity"].rolling(window=10).mean()
    df_fastball["PitchOrder"] = df_fastball.index



    plt.figure(figsize=(10,5))
    plt.plot(df_fastball["No"], df_fastball["Rolling Velo"], marker="o", linestyle="-", label="Rolling 10-Pitch Fastball Velo")
    plt.xlabel("No")
    plt.ylabel("Velocity (mph)")
    plt.title("Rolling 10-Pitch Average Velocity (Fastballs)")
    plt.legend()
    plt.grid(True)
    num_ticks = 5
    plt.xticks(df_fastball["Date"][::len(df_fastball)//num_ticks], rotation=20)
    plt.show()


def main():
    df = load_data("/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/Ananth_Data/940780_pitching_57b97b91a69622a54767.csv")
    rollingFastballVelo(df)



if __name__ == "__main__":
        main()
