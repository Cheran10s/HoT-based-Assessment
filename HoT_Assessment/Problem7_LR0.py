import pandas as pd
df=pd.DataFrame({"Items":[10,20,15]})
avg=df["Items"].mean()
print("Average:",avg)
print("Is_State_Explosion:",avg>12)