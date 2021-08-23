import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')

#print(df.columns)

BMI = df['weight']/((df['height']/100)**2)

BMI[BMI>25] = 1
BMI[BMI!=1] = 0

# Add 'overweight' column
df['overweight'] = BMI
df['overweight'] = df['overweight'].astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.



df['cholesterol'].loc[df['cholesterol'] == 1] = 0

df['cholesterol'].loc[df['cholesterol'] != 0] = 1

df['gluc'].loc[df['gluc'] == 1] = 0

df['gluc'].loc[df['gluc'] != 0] = 1 

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df, id_vars = 'cardio', value_vars =  ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat['valor'] = df_cat['value']
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat = df_cat.groupby(['cardio', 'variable', 'valor'], as_index = False).count()

    # Draw the catplot with 'sns.catplot()'


    fig = sns.catplot(x = 'variable', y = 'value', hue = 'valor', col = 'cardio', data = df_cat, kind="bar") 

    fig.set_axis_labels("variable", "total")
    fig._legend.set_title('value')
    print(type(fig))

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    '''df_heat = df[df['ap_lo'] <= df['ap_hi']]



    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]



    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]



    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]



    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]'''

    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask_1 = np.zeros_like(corr)

    mask_1[np.triu_indices_from(mask_1)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'

    ax = sns.heatmap(corr, mask = mask_1, annot = True, fmt = '.1f', center = 0, vmin = -0.1, vmax = 0.3, linewidths=0.5, square = True)



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    print(type(fig))
    return fig
