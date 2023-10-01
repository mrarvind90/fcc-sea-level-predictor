import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir[:-3], "data/epa-sea-level.csv")
    output_dir = os.path.join(script_dir[:-3], "output")

    df = pd.read_csv(data_dir, encoding="utf-8")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    x1 = np.arange(df["Year"].min(), 2051, 1)
    y1 = line1.intercept + line1.slope * x1
    plt.plot(x1, y1, color="firebrick")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]

    line2 = linregress(x=df_2000["Year"], y=df_2000["CSIRO Adjusted Sea Level"])
    x2 = np.arange(df_2000["Year"].min(), 2051, 1)
    y2 = line2.intercept + line2.slope * x2
    plt.plot(x2, y2, color="mediumseagreen")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    plt.savefig(output_dir + "/sea_level_plot.png")

    return plt.gca()


draw_plot()
