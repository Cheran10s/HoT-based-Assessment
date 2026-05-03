import pandas as pd
df=pd.DataFrame({"Expr":["a+b","a+b","x+y"]})
freq=df["Expr"].value_counts().reset_index()
freq.columns=["Expr","Frequency"]
freq["Is_Common_Subexpression"]=freq["Frequency"]>1
print(freq)