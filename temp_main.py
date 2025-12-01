# temp main file for data analysis project
#import the necessary packages
import numpy as np #for data processing
import pandas as pd #csv file IO
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#import the csv file "covid_19_india.csv"
covid_df = pd.read_csv("covid_19_india.csv")
print("Dataset Information")
print(covid_df.info())
print("\nMissing Data Information")
print(covid_df.isna().sum())
print("\n------------------------------------------------------------------------------")
print("To get the number of deaths, confirmed, and cured cases state wise")
covid_df['Active'] = covid_df['Confirmed'] - covid_df['Cured'] - covid_df['Deaths']
count = covid_df.groupby("State/UnionTerritory")[['Confirmed','Deaths','Cured','Active']].sum().reset_index()
print(count)
print("\n------------------------------------------------------------------------------")
print("\nTo get the mortality rates and recovery rates of all states and display them in a pivot table analysis")
state_df = pd.pivot_table(covid_df, values=['Confirmed', 'Deaths', 'Cured', 'Active'], index=['State/UnionTerritory'], aggfunc="max")
state_df['Recovery Rate'] = state_df['Cured']*100/state_df['Confirmed']
state_df['Mortality Rate'] = state_df['Deaths']*100/state_df['Confirmed']
state_df=state_df.sort_values(by="Confirmed",ascending=False)
print(state_df)
print("\n------------------------------------------------------------------------------")
print("\nTo display Top 10 states with Active cases")
top10ActiveCases=covid_df.groupby(by='State/UnionTerritory').max()[['Active','Date']].sort_values(by=['Active'],ascending=False).reset_index()
fig=plt.figure(figsize=(16, 10))
plt.title("Top 10 states with most Active Cases  in India",size=22)
ax=sns.barplot(data=top10ActiveCases.iloc[:10],y='Active',x='State/UnionTerritory',linewidth=2,edgecolor='black', hue='State/UnionTerritory')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()

print("\n------------------------------------------------------------------------------")
# print("\nTo display the growth trend in as line graph for top 5 states ")
fig=plt.figure(figsize=(12,6))
ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pradesh'])],x='Date',y='Active',hue='State/UnionTerritory')
ax.set_title("Top 5 Affected States in India",size=16)
plt.show()

print("\n------------------------------------------------------------------------------")
print("\nTo show top Months of 2020 for spike in covid cases")
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format="%Y-%m-%d")
covid_df_new = covid_df[covid_df['Date'].dt.year == 2020]
covid_df_new['Date'] = pd.to_datetime(covid_df_new['Date'], format='%Y-%m-%d')
covid_df_new['Month'] = covid_df_new['Date'].dt.month_name()
topmonths = covid_df_new.groupby(by='Month').max()[['Confirmed','Date']].sort_values(by=['Confirmed'],ascending=False).reset_index()
fig=plt.figure(figsize=(12,6))
ax=sns.lineplot(data=topmonths.iloc[:5],x='Month',y='Confirmed')
ax.set_title("Top 5 Affected Months in 2020",size=16)
plt.show()
print("\n------------------------------------------------------------------------------")
print("\nTo show top Months of 2021 for spike in covid cases")
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format="%Y-%m-%d")
covid_df_new = covid_df[covid_df['Date'].dt.year == 2021]
covid_df_new['Date'] = pd.to_datetime(covid_df_new['Date'], format='%Y-%m-%d')
covid_df_new['Month'] = covid_df_new['Date'].dt.month_name()
topmonths = covid_df_new.groupby(by='Month').max()[['Confirmed','Date']].sort_values(by=['Confirmed'],ascending=False).reset_index()
fig=plt.figure(figsize=(12,6))
ax=sns.lineplot(data=topmonths.iloc[:5],x='Month',y='Confirmed')
ax.set_title("Top 5 Affected Months in 2021",size=16)
plt.show()