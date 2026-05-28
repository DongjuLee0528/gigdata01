import seaborn as sns
import matplotlib.pyplot as plt


# 피실험자, 측정시간, 자극종류, 뇌부위, 뇌측정신호
fmri = sns.load_dataset("fmri")
# print(fmri.head())
# print(fmri.tail())
# print(fmri.describe())
# print(fmri.info())
# print(fmri.groupby(['region', 'event'])['signal'].mean())
# print(fmri.groupby(['region', 'event'])['signal'].std())
# print(fmri.groupby(['region', 'event'])['signal'].max())
# print(fmri.groupby(['region', 'event'])['signal'].min())
print(fmri.groupby(['region', 'event'])['signal'].agg(['mean', 'std', 'max', 'min']))
# print(high_spending['Country'].unique())
# 국가별 평균 의료비 지출과 평균 기대수명 구하기
# country_mean = health.groupby('Country')[['Spending_USD', 'Life_Expectancy']].mean()
# print(country_mean)
# 국가별로 데이터가 몇 개씩 있는지 개수 세기
# print(health['Country'].value_counts())
# 년도별 평균 의료비 지출과 평균 기대수명 구하기
# year_mean = health.groupby('Year')[['Spending_USD', 'Life_Expectancy']].mean()
# print(year_mean)
# 국가별 기대수명 분포 확인
# sns.catplot(data=health, x='Year', y='Life_Expectancy', col='Country', kind='box', col_wrap=3)
# plt.show()
# 가장 최근(2020년) 국가별 의료비 지출 비교
# sns.catplot(data=health_2020, x='Country', y='Spending_USD', kind='bar', palette='muted')
# plt.show()
# 국가별 의료비와 기대수명의 상관관계 (산점도)
# sns.relplot(data=health,
#             x='Spending_USD',
#             y='Life_Expectancy',
#             col='Country',
#             col_wrap=3,
#             kind='scatter',
#             hue='Year',
#             palette='Set1'
#             )
# plt.show()

# print(health.sort_values('Year', ascending=False))
# 2가지 기준으로 정렬 (년도별 순, 그다음 기대수명 높은 순)후 상위 10개 데이터 출력
# print(health.sort_values(['Year','Life_Expectancy'], ascending=[False, False]).head(10))