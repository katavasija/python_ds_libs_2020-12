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

