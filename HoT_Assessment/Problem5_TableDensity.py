import pandas as pd
df=pd.DataFrame({"Entries":[20],"Size":[25]})
df["Density"]=df["Entries"]/df["Size"]
df["Is_Table_Complex"]=df["Density"]>0.7
print(df)