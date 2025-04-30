# 02.1 Script with python
# print("Hello World")

# 02.2 Import
import pandas as pd

# data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame)

# 04 Series
# numbers_data = [23,45,7,34,6,63,36,78,54,34]
# numbers_series = pd.Series(numbers_data)
#print(numbers_series)

# 04.1 Date Range
# pd_daterange = pd.date_range(start="2021-05-01", end="2021-05-12")
# print(pd_daterange)

# 04.2 Series Apply
# my_series = pd.Series([2, 4, 6, 8, 10])
# my_series_slices = my_series.apply(lambda x: x / 2)
# print(my_series_slices)

# 05 DataFrames
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
# df_cars = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
# print(df_cars)

# 05.1 DataFrame Dict
# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla",
#         "model": "Model S",
#         "color": "Red"
#     }
# ]

# df_carsbrands = pd.DataFrame.from_dict(data)
# print(df_carsbrands)

# 05.2 DataFrame iLoc
# df_poke = pd.read_csv(".learn/assets/pokemon_data.csv")
# df_cells = df_poke.iloc[133, 6]
# print(df_cells)

# 05.3 DataFrame Head
# df_head = df_poke.head(3)
# print(df_head)

# 05.4 DataFrame Tail
# df_tail = df_poke.tail(3)
# print(df_tail)

# 05.5 Print Columns
# df_columns = df_poke[["Name", "Type 1"]][0:10]
# print(df_columns)

# 05.6 Loc Function
# df_loc_func = df_poke.loc[df_poke["Attack"] > 80]
# print(df_loc_func)

# 05.7 Filter and Count
# pd_poke_legendary= df_poke.loc[df_poke["Legendary"] == True]
# legendaries_count = len(pd_poke_legendary)
# print(legendaries_count)

# 06 Clean Datasets 
df_baby_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")
# print(df_baby_names.head(5))

# 06.1 Remove Column 
# df_remove_column = df_baby_names.drop(columns=["Unnamed: 0"])
# print(df_remove_column.head(5))

# 06.2 Value Counts
# df_value_counts = df_baby_names.value_counts("Gender")
# print(df_value_counts)

# 06.3 Group By
df_group_by = df_baby_names.groupby








