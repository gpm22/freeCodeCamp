import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    
    fig, ax1 = plt.subplots()
    
    df.plot.scatter(x = 'Year', y = 'CSIRO Adjusted Sea Level' , ax=ax1)


    # Create first line of best fit
    
    res_1 = linregress( x = df.Year, y = df['CSIRO Adjusted Sea Level'])
    
    x_1 = np.arange(df.Year.iloc[0], 2051)
    
    y_1 = x_1*res_1.slope + res_1.intercept
    
    ax1.plot(x_1,y_1, c = 'green')


    # Create second line of best fit
    
    df_new = df.loc[df.Year >= 2000]
    
    res_2 = linregress( x = df_new.Year, y = df_new['CSIRO Adjusted Sea Level'])
    
    x_2 = np.arange(df_new.Year.iloc[0], 2051)
    
    y_2 = x_2*res_2.slope + res_2.intercept
    
    ax1.plot(x_2,y_2, c = 'red')
    
    # Add labels and title
    
    ax1.set(xlabel = 'Year', ylabel='Sea Level (inches)', title = 'Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()