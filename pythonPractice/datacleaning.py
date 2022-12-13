import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/krishnanchandran/Downloads/netflix_titles.csv')

df.info()

df.dropna(inplace=True)  # Drops null values in cols
df.drop_duplicates(inplace=True)
df.info()

# print(df.to_string())

df.to_csv('/Users/krishnanchandran/Downloads/netflix_titles9.csv')  # After removing stores in csv form netflix_titles9

df = pd.read_csv('/Users/krishnanchandran/Downloads/netflix_titles9.csv')
df.plot(kind='scatter', x='release_year', y='type')  # graph
plt.show()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2020", periods=1000))
# ts = ts.cumsum()
# ts.plot();
