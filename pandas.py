%matplotlib inline
import numpy as np
import pandas as pd

dataFrame = pd.read_csv("past-hires.csv")
df = dataFrame

df.head() # returns an initial set of data from the loaded file

df.head(10) # returns a specific amount of rows from the data frame that was loaded

df.tail(4) # returns the end of the data set - in this case the last 4 rows

df.shape # returns the dimension of the data frame or shape of the data frame

df.size # returns the size, i.e the number of columns * the number of rows

len(df) # returns the number of rows

df.columns # returns a list with all the data frame column names

df['Hired'] # extracts a single column from the data frame - returns a "series" in Pandas

df["Hired"][:5] # extracts a given range from the name column (first five rows)

df[:Hired"][5] # extracts an exact row in the column

df[["Hired", "Years Experience"]] # extracts multiples columns

df[["Hired", "Years Experience"]][:5] # extracts a specific range for the columns

df.sort_values(["Years Experience"]) # sorts by

degree_counts = df['Level of Education'].value_counts() # break down the number of unique values in a given column into a Series - good for understanding the distribution of the data

degree_counts

degree_counts.plot(kind='bar')

# Exercise
# Try extracting rows 5-10 of our DataFrame, preserving only the "Previous employers" and "Hired" columns. Assign that to a new DataFrame,
# and create a histogram plotting the distribution of the previous employers in this subset of the data.

plot_distribution = df[['Previous employers', 'Hired']][5:11]
plot_distribution.plot(kind="hist")
