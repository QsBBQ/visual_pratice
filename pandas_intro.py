import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

print(df.head())
print(df.tail())
print(df.tail(2))

# Now we want to set a index
df.set_index('Day', inplace=True)
print(df.head)
print(df["Visitors"])
print(df[['Visitors','Bounce Rate']])

df['Visitors'].plot()
plt.show()
