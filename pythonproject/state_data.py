#use three csv files, calculate the population density of each state in America
#merge three files into one
import numpy as np
import pandas as pd
pop = pd.read_csv("/Users/liaodisen/Desktop/state-population.csv")
areas = pd.read_csv("/Users/liaodisen/Desktop/state-areas.csv")
abbrevs = pd.read_csv("/Users/liaodisen/Desktop/state-abbrevs.csv")

pop_merged = pd.merge(pop, abbrevs, left_on="state/region", right_on="abbreviation", how="outer")
pop_merged = pop_merged.drop('abbreviation', axis=1)

#state and region is NAN in this two regions
pop_merged.loc[pop_merged['state/region']== 'PR', 'state'] = 'Puerto Rico'
pop_merged.loc[pop_merged['state/region']== 'USA', 'state'] = 'United States'

#combine areas into the table and delete the lines that have no data
result = pd.merge(pop_merged, areas, on='state', how='left')
result.dropna(inplace = True)

#calculate the population density of 2012
d2012 = result.query("year==2012 & ages == 'total'")
d2012.set_index('state', inplace = True)
density = d2012['population'] / d2012['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
density.to_csv("state_density_sorted", header=[''])
