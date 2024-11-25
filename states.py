import pandas as pd

states =["California", "Texas", "Florida", "New York"]
population = [1234, 5678, 9087, 6543]
dict_states = {'States': states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
df_states.to_csv('states.csv', index=False)










# print (states[-4])

# for state in states:
#     if state == "Florida":
#         print(state)


with open('export-data.txt', 'w') as file:
    file.write("Data successfully scraped!")
