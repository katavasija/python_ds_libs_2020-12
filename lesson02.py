# coding: utf-8

# """
# task1
# Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: 
# [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные: 
# [1, 1, 1, 2, 2, 3, 3], 
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# """

# In[1]:
import pandas as pd

# In[2]:
authors = pd.DataFrame({'author_id': [1, 2, 3], 'author_name': ['Тургенев', 'Чехов', 'Островский']
                       }, columns=['author_id', 'author_name']
                      )

# In[3]:
books = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                                   'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]
                    }, columns = ['author_id', 'book_title']
)

# """
# task2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# """

# In[4]:
authors_price = pd.merge(authors, books, on = 'author_id', how = 'inner')

# """
# task3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
# """

# In[5]:
top5 = authors_price.sort_values(by='price', ascending=False).head(5)
top5.reset_index(drop = True)

# """
# task4
# Создайте датафрейм authors_stat на основе информации из authors_price. 
# В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно 
# имя автора,минимальная, максимальная и средняя цена на книги этого автора
# """

# In[6]:
authors_stat = authors_price.groupby(['author_name']).agg({
	 'price': ['min', 'max', 'mean']
}).reset_index()
authors_stat.columns = ['author_name', 'min_price', 'max_price', 'mean_price']
authors_stat

# """
# task5
# Создайте новый столбец в датафрейме authors_price под названием cover, 
# в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. 
# В этот столбец поместите данные из следующего списка:
# ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
# Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. 
# При этом столбцы должны 
# называться "твердая" и "мягкая", а индексами должны быть фамилии авторов.
# Пропущенные значения стоимостей заполните нулями.
# Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl".
# Затем загрузите из этого файла датафрейм и назовите его book_info2. 
# Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
# """

# In[7]:
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price

# In[8]:
import numpy as np

# In[9]:
book_info = pd.pivot_table(authors_price, 
                           values='price', 
                           index=['author_name'], 
                           columns=['cover'], 
                           aggfunc=np.sum, 
                           fill_value=0)
book_info

# In[10]:
book_info.to_pickle("./book_info.pkl")

# In[11]:
book_info2 = pd.read_pickle("./book_info.pkl")
book_info2
