
import pandas as pd
import matplotlib as plt

#الطلب الأول

dic={'math':[50,45,80,65],'prog':[51,45,72,84],'electric':[46,91,73,42]}
std= ["ahmed","ali","maha","sara"]
df= pd.DataFrame(dic,index=std)

df.loc['rabee']=[30,20,40]

df["max"]=df.max(axis=1)
df["min"]=df.min(axis=1)
df["ave"]=df[['math','prog','electric']].mean(axis=1)

def update_mark(df,name,s,d):
    df.loc[name,s]=d
    return df
df=update_mark(df,'ahmed','math',100)
df['result']=df['ave'].apply(lambda x: 'pass' if x>50 else 'fail')
df['new prog']=df['prog'].apply(lambda x: x+10)



print(df)
df1=df.query('ave>50')
print(df1)


