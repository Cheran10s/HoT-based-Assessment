import pandas as pd
df=pd.DataFrame({"Block":[1,1,2],"Temp":["t1","t2","t3"]})
temp=df.groupby("Block").size().reset_index(name="Temp_Count")
temp["Is_Temp_Heavy"]=temp["Temp_Count"]>2
print(temp)