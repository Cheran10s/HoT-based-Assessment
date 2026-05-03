import pandas as pd
df=pd.DataFrame({"Function":["f1","f2"],"Size":[500,2000]})
df["Is_Stack_Overflow_Risk"]=df["Size"]>1000
print(df)