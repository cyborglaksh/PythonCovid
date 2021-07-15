# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px


# %%
df = pd.read_csv('./country_wise_latest.csv')
df

# %%
df.drop(columns = ['Active','WHO Region','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','Confirmed last week','1 week change','1 week % increase'],axis = 1,inplace=True)


# %%
df

# %%
df.isnull().sum()

# %%
x = 50
y = 60

# %%
country = list(df['Country/Region'][x:y])
confirmed = list(df['Confirmed'][x:y])
deaths = list(df['Deaths'][x:y])
recovered = list(df['Recovered'][x:y])

# %%
w = 0.2
bar1 = np.arange(len(country))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]


# %%
plt.figure(figsize=(20,20))
plt.bar(bar1,confirmed,w,label="Confirmed")
plt.bar(bar2,deaths,w,label="Deaths")
plt.bar(bar3,recovered,w,label="Recovered")


plt.xlabel("Countries")
plt.ylabel("Status")
plt.title("Corona Statistics")
plt.xticks(bar1+w,country)
plt.legend()
plt.show()


# %%


# %%
