import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Spending_USD': [2000, 4000, 6000, 8000],
    'Life_Expectancy': [70, 75, 80, 82]
})

sns.relplot(
    data=df,
    x='Spending_USD',
    y='Life_Expectancy',
    kind='scatter'
)

plt.show()