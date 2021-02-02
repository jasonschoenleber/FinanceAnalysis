import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = 'jira.xlsx'

df = pd.read_excel(excel_file_path)
print(df.columns)

df_info = df.info()
print(df_info)

print(df.describe()['Status'])

pivot_done = df.groupby(['Status']).count()
status_count = pivot_done.loc[:,"Priority"]

status_count.plot(kind='bar')
plt.show()

status_count.to_excel('output.xlsx', sheet = 'test')
