import pandas as pd
df=pd.DataFrame({"FIRST":[{"a","b"}],"FOLLOW":[{"b"}]})
df["Overlap"]=df.apply(lambda x: len(x["FIRST"]&x["FOLLOW"]),axis=1)
df["Is_LL1_Violated"]=df["Overlap"]>0
print(df)