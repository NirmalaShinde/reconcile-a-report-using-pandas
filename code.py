# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
print(df.head(5))
df['state'] = df['state'].str.lower()
print(df.head(3))

df['total'] = df["Jan"] + df["Feb"] + df["Mar"]

sum_row=df[["Jan","Feb","Mar","total"]].sum()
print(sum_row)
df_sum=pd.DataFrame(data=sum_row).T
df_final=df.append(df_sum,ignore_index=True)
df_final.tail()

# Code ends here


# --------------
import requests

# Code starts here
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]

df1.columns = df1.iloc[11]
df1 = df1.iloc[12:]
df1['United States of America'] = df1['United States of America'].apply(lambda x:x.replace(" ",""))

# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here

mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr', np.nan)
df_final['abbr'] = df_final['state'].map(mapping)


# Code ends here


# --------------
# Code stars here
df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')
df_tenessee  = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')
df_final.replace(df_final.iloc[6],df_mississipi,inplace = True)
df_final.replace(df_final.iloc[10],df_tenessee,inplace = True)
# Code ends here


# --------------
# Code starts here

df_sub = df_final.groupby('abbr')[['Jan','Feb','Mar','total']].sum()
formatted_df = df_sub.applymap(lambda x: str(x) + '$') 

# Code ends here


# --------------
# Code starts here

sum_row = pd.DataFrame(df_final[['Jan', 'Feb', 'Mar', 'total']].sum(),index=['Jan', 'Feb', 'Mar', 'total'])
df_sub_sum = sum_row.T
df_sub_sum = df_sub_sum.applymap(lambda x:"$"+str(x))
final_table = formatted_df.append(df_sub_sum)
print(final_table)
final_table.rename(index={0:'Total'}, inplace=True)

# Code ends here


# --------------
# Code starts here

df_sub['total'] = df_sub['total'].sum()
df_sub['total'].plot.pie(figsize=(5, 5))

# Code ends here


