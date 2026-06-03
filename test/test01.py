import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'pclass': [1, 2, 3],
    'survived': [0.63, 0.47, 0.24]
})

sns.barplot(
    data=df,
    x='pclass',
    y='survived'
)

plt.show()