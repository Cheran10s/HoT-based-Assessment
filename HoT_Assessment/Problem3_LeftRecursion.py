import pandas as pd
df=pd.DataFrame({"Rule":["A->Aα","B->b"]})
df["Has_Left_Recursion"]=df["Rule"].apply(lambda x: x.split("->")[0] in x.split("->")[1])
print(df)