import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'time': ['10 min', '20 min', '30 min', '10 min', '20 min', '30 min'],
    'pulse': [80, 90, 100, 75, 85, 95],
    'diet': ['low fat', 'low fat', 'low fat',
             'high fat', 'high fat', 'high fat']
})

sns.catplot(
    data=df,
    x='time',
    y='pulse',
    hue='diet',
    kind='point'
)

plt.show()