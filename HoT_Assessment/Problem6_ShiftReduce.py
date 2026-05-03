import pandas as pd
df=pd.DataFrame({"State":[1,1],"Conflict":[1,1]})
conf=df.groupby("State")["Conflict"].sum().reset_index()
conf["Is_Conflict_Prone"]=conf["Conflict"]>1
print(conf)