import pandas as pd
df = pd.DataFrame({"File":["A.c","B.c"],"Identifier":["sum","x"]})
df["Length"]=df["Identifier"].apply(len)
avg=df.groupby("File")["Length"].mean().reset_index()
avg["Is_Poor_Naming"]=avg["Length"]<3
print(avg)