import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date')

df.index = pd.to_datetime(df.index)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax1 = plt.subplots()
    
    df.plot.line(ax=ax1, legend = False)
    ax1.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax1.set(xlabel = 'Date', ylabel = 'Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot(): 
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['Years'] = [d.year for d in df_bar.date]
    #df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%m') for d in df_bar.date]
    
    #df_bar = df_bar.groupby(['Months', 'Years'], as_index = False).mean() 

    df_bar = df_bar.groupby(['Years', 'Months']).mean()
    
    df_bar = df_bar.unstack()
    
    months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 

    # Draw bar plot
    
    '''fig = sns.catplot(x = 'Years', y = 'value', hue = 'Months', data= df_bar, kind = 'bar', hue_order = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    fig.set_axis_labels("Years", "Average Page Views")'''

    fig, ax = plt.subplots()
    
    df_bar.plot.bar(ax=ax)
    
    ax.set(xlabel = 'Years', ylabel = 'Average Page Views')
    ax.legend(labels=months, title = 'Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

       
    # Draw box plots (using Seaborn)
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    
    sns.boxplot(x=df_box['Year'], y=df_box['value'], ax=ax1)
    
    sns.boxplot(x=df_box['Month'], y=df_box['value'], order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=ax2)

    ax1.set(ylabel = 'Page Views', title = 'Year-wise Box Plot (Trend)')
    ax2.set(ylabel = 'Page Views', title= 'Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
