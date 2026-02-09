import pandas as pd

df = pd.read_excel('Covid Dashboard.xlsx', sheet_name='Data')
data_2d_array = df.values.tolist()

columns = df.columns.tolist()
print("Columns:", columns)
print("-" * 20)
print("First 10 Rows of the spreadsheet")

for i in range(min(10,len(data_2d_array))):
    print("Row ", i, ":", data_2d_array[i])
print("-" * 20)
print("Last 10 Rows of the spreadsheet")

total_rows = len(data_2d_array)
start_index = max(0, total_rows - 10)

for i in range(start_index, total_rows):
    print("Row ", i, ":", data_2d_array[i])