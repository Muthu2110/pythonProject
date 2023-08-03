import pandas as pd
import matplotlib.pyplot as plt
import pandasql as psql
import csv

df = pd.read_csv('/Users/krishnanchandran/Downloads/netflix_titles.csv')

df.info()

df.dropna(inplace=True)  # Drops null values in cols
df.drop_duplicates(inplace=True)
df.info()

# print(df.to_string())

df.to_csv('/Users/krishnanchandran/Downloads/netflix_titles9.csv')  # After removing stores in csv form netflix_titles9

cdf = psql.sqldf("select show_id,country from df")
print("######")
print(cdf)
print("######")
print("########")

listOfCountries = cdf.values.tolist  # converting new cdf(dataframe) to a list

resultDictionary = [] #created a empty list
uniqueCountryList = set() # set() has no duplicates
print(cdf.values.tolist())
print("######")
studentsDict = dict(cdf.values.tolist())
# print(studentsDict)
print("#######")
print(studentsDict['s8'].split(", "))
# for each values, create a new dic with country as key and value as showID
keys = studentsDict.keys()
for showId in keys:
    countryList = studentsDict[showId].split(", ")
    for country in countryList:
        uniqueCountryList.add(country)
        resultDict = {country: showId}
        resultDictionary.append(resultDict)

print("$$$$$$")
print(uniqueCountryList)
print("$$$$$$")
print(resultDictionary)

print("$$$$$$SS")

i = 0

list1 = []
for i in range(8807):
    list1.append(0)

i = 0
for country in uniqueCountryList:
    if country != '':
        i = i + 1
        # print(i)
        st = str(country)
        # print(st)
        jdf = pd.Series(list1).rename(country)
        df = pd.concat((df, jdf), axis=1)

print(i)
df.info()
print("HHHHH")
i = 0
indexList = psql.sqldf("select show_id from df").values.tolist()
resultIndexList = map(lambda x: x[0], indexList)
print("gggg")
s = list(resultIndexList)
# print(s)
df.set_index('show_id')
# df.index = list(resultIndexList)
# for r in s:
#     print(r)
#
#     s = psql.sqldf("select * from df where show_id='" + str(r)+"'")
#     print(s)
# print(df.loc[df['show_id'] == 's8'])
# print(df)
df.dropna(inplace=True)
dictList = []
with open('/Users/krishnanchandran/Downloads/dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for x in resultDictionary:
        key = list(x.keys())[0]
        ffdf = df.loc[(df['show_id'] == str(x.get(key)))]
        # ffdf.__getitem__(str(key)).__setitem__(0, 1)
        print(str(key))
        print(str(x.get(key)))
        writer.writerow([str(key), str(x.get(key))])
        if str(key) == '':
            continue
        row = ffdf.__getitem__(str(key)).index.values[0]
        print(row)
        df.at[row, (str(key))] = 1

df.to_csv('/Users/krishnanchandran/Downloads/netflix_titles2.csv')  # After removing stores in csv form netflix_titles9
# dictDF.to_csv('/Users/krishnanchandran/Downloads/netflix_titles3.csv')
# df.plot(kind='scatter', x='release_year', y='type')  # graph
# plt.show()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2020", periods=1000))
# ts = ts.cumsum()
# ts.plot();
