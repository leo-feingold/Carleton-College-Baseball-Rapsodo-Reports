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


def parse_files():
    files = ["/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/anath_iyer/940780_pitching_e5da2b57c63722e5fac6.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/dan_avillo/1170315_pitching_a293c34fdd06898d6608.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/eli_travis/1338288_pitching_600371766e00635409aa.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/ethan_chan/1075743_pitching_cd91e5efa0433c7da6ba.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/jackson_corcoran/1075741_pitching_3933f41138db38245064.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/jake_stern/1075930_pitching_a5af1596c845f54ac2e9.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/jordan_kramer/1075756_pitching_8ade13e92d680298f08e.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/mark_fernandez/941242_pitching_a7073ebcfcb8a1548020.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/quinn_brannan/940677_pitching_4dbc1d5aa1098aa7b338.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/ryan_chang/1075661_pitching_d980dbc36788489b412b.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/sam_chutkow/1076782_pitching_645dbd8be515872cc0b7.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/sam_zacks/940794_pitching_e70d247d76476acf51fc.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/william_schnepf/1075665_pitching_1b98bb75ab4f20fd16eb.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/xander_stolberg/1348694_pitching_50e7a40dcf087b94ae6d.csv",
            "/Users/leofeingold/Documents/GitHub/Carleton-College-Baseball-Rapsodo-Reports/zachary_gordon/978916_pitching_9220f83c0ab5ba79fad4.csv"
    ]

    dfs = []
    for file in files:
        df = load_data(file)
        dfs.append(df)

    return dfs

def concat_data(dfs):
    combined_data = pd.concat(dfs)
    return combined_data


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

def rolling_fastball_velo(df):

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

def calc_averages_by_pitch(df):
    df["Velocity"] = pd.to_numeric(df["Velocity"], errors="coerce")
    df["VB (trajectory)"] = pd.to_numeric(df["VB (trajectory)"], errors="coerce")
    df["HB (trajectory)"] = pd.to_numeric(df["HB (trajectory)"], errors="coerce")
    df["VB (spin)"] = pd.to_numeric(df["VB (spin)"], errors="coerce")
    df["HB (spin)"] = pd.to_numeric(df["HB (spin)"], errors="coerce")
    df["Total Spin"] = pd.to_numeric(df["Total Spin"], errors="coerce")
    df["True Spin (release)"] = pd.to_numeric(df["True Spin (release)"], errors="coerce")
    df["Spin Efficiency (release)"] = pd.to_numeric(df["Spin Efficiency (release)"], errors="coerce")
    

    return df.groupby("Pitch Type").agg({
        "Velocity": "mean",
        "VB (trajectory)": "mean",
        "HB (trajectory)": "mean",
        "VB (spin)": "mean",
        "HB (spin)": "mean",
        "VB (spin)": "mean",
        "HB (spin)": "mean",
        "Total Spin": "mean",
        "True Spin (release)": "mean",
        "Spin Efficiency (release)": "mean",

    }).reset_index()

    '''
        "VB (spin)": "mean",
        "HB (spin)": "mean",
        "Total Spin": "mean",
        "True Spin (release)": "mean",
        "Spin Efficiency (release)": "mean",
        #"Spin Direction": "mean",
        "Spin Confidence": "mean"
    '''


def bar_graph_velo(df):
    df = df[df["Pitch Type"] == "Fastball"]
    bins = pd.cut(df["Velocity"], 8)
    bin_counts = bins.value_counts().sort_index()
    bin_labels = [str(interval) for interval in bin_counts.index]
    
    plt.figure(figsize = (10, 8))
    plt.bar(bin_labels, bin_counts, color="royalblue", edgecolor="black")
    plt.xlabel("Velocity Range")
    plt.ylabel("Count of Pitches in Range")
    plt.title("Fastball Velocity Distribution, High Intent Bullpens and Live ABs, (Jan-March 2025)")
    plt.xticks(rotation = 30)
    plt.show()

    



def main():
    dfs = parse_files()
    data = concat_data(dfs)
    averages = calc_averages_by_pitch(data)
    #print(averages)
    bar_graph_velo(data)



if __name__ == "__main__":
        main()
