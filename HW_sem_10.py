# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

new_data = data.copy()
list_whoAmI = data['whoAmI'].tolist()
new_columns = list(set(list_whoAmI))
for column in new_columns:
    for characteriscic in list_whoAmI:
        new_data.loc[new_data['whoAmI'] == column, column] = '1' 

del new_data['whoAmI']
new_data = new_data.fillna(0)
print(new_data)

