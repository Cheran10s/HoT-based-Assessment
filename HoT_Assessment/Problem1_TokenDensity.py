import pandas as pd
df = pd.DataFrame({"File":["A.c","A.c","B.c"],"Line":[1,2,1],"Token":["int","main","x"]})
tpl = df.groupby(["File","Line"]).size().reset_index(name="Token_Count")
density = tpl.groupby("File")["Token_Count"].mean().reset_index()
density["Is_Token_Heavy"] = density["Token_Count"] > 2
print(density)