
import matplotlib.pyplot as pt
import pandas as pd
df = pd.read_csv(r'C:\Users\bella\OneDrive\Documents\data_set.csv')
df.head(1)
print(df)

ram = df['RAM (in GB)']
print(ram)
pt.hist(ram)

pt.xlabel('RAM')
pt.ylabel('count')
pt.title("DATA")
pt.show()