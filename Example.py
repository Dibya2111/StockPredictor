# import pandas as pd
# ds= pd.Series([2,4,6,8,10])
# print(ds)
# Output: 
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64

# print("Pandas Series And Type:")
# print(ds)
# print(type(ds))
# print("PAndas Series AS List")
# print(ds.tolist())
# print(type(ds.tolist()))
# Output:
# Pandas Series And Type:
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64
# <class 'pandas.core.series.Series'>
# PAndas Series AS List
# [2, 4, 6, 8, 10]
# <class 'list'>

# s1=pd.Series([2,4,6,8,10])
# s2=pd.Series([1,3,5,7,9])
# s=s1+s2
# print("Add Two Series:")
# print(s)
# print("Subtract Two Series:")
# s=s1-s2
# print(s)
# print("Multiply Two Series:")
# s=s1*s2
# print(s)
# print("Divide Series1 by Series2:")
# s=s1/s2
# print(s)
# Output:
# Add Two Series:
# 0     3
# 1     7
# 2    11
# 3    15
# 4    19
# dtype: int64
# Subtract Two Series:
# 0    1
# 1    1
# 2    1
# 3    1
# 4    1
# dtype: int64
# Multiply Two Series:
# 0     2
# 1    12
# 2    30
# 3    56
# 4    90
# dtype: int64
# Divide Series1 by Series2:
# 0    2.000000
# 1    1.333333
# 2    1.200000
# 3    1.142857
# 4    1.111111
# dtype: float64

# import pandas as pd
# import numpy as np
# np_array=np.array([10,20,30,40,50])
# print("Numpy Array:")
# print(np_array)
# ds=pd.Series(np_array)
# print("Pandas Series:")
# print(ds)
# Output:
# Numpy Array:
# [10 20 30 40 50]
# Pandas Series:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int32

# import pandas as pd
# data={
#     'apple':[10,20,30,40,50],
#     'banana':[10,20,30,40,50],
#     'orange':[10,20,30,40,50]
# }
# purchases=pd.DataFrame(data)
# print(purchases)
# Output:
#  apple  banana  orange
# 0     10      10      10
# 1     20      20      20
# 2     30      30      30
# 3     40      40      40
# 4     50      50      50

# import pandas as pd
# data={
#     'apple':[10,20,30,40,50],
#     'banana':[10,20,30,40,50],
#     'orange':[10,20,30,40,50]
# }
# purchases=pd.DataFrame(data,index=['John','Alice','Bob','Mary','Tom'])
# print(purchases)
# Output:
#        apple  banana  orange
# John      10      10      10
# Alice     20      20      20
# Bob       30      30      30
# Mary      40      40      40
# Tom       50      50      50

# import pandas as pd
# orders=pd.read_table('http://bit.ly/chiporders')
# print(orders.head())
# Output:
#    order_id  quantity                              item_name                                 choice_description item_price
# 0         1         1           Chips and Fresh Tomato Salsa                                                NaN     $2.39 
# 1         1         1                                   Izze                                       [Clementine]     $3.39 
# 2         1         1                       Nantucket Nectar                                            [Apple]     $3.39 
# 3         1         1  Chips and Tomatillo-Green Chili Salsa                                                NaN     $2.39 
# 4         2         2                           Chicken Bowl  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98 

# import pandas as pd
# orders=pd.read_table('http://bit.ly/chiporders')
# orders.drop('choice_description',axis=1,inplace=True)
# print(orders.head())
# Output:
#    order_id  quantity                              item_name item_price
# 0         1         1           Chips and Fresh Tomato Salsa     $2.39 
# 1         1         1                                   Izze     $3.39 
# 2         1         1                       Nantucket Nectar     $3.39 
# 3         1         1  Chips and Tomatillo-Green Chili Salsa     $2.39 
# 4         2         2                           Chicken Bowl    $16.98

# import pandas as pd
# user_cols=['user_id','age','gender','occupation','zip_code']
# users=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_cols)
# print(users.head())
# Output:
#    user_id  age gender  occupation zip_code
# 0        1   24      M  technician    85711
# 1        2   53      F       other    94043
# 2        3   23      M      writer    32067
# 3        4   24      M  technician    43537
# 4        5   33      F       other    15213

# import pandas as pd
# user_cols=['Student_ID','Student Name','Age','Gender','Marks(Out Of 100)']
# users=pd.read_csv('./AssignmentSkillLab.csv')
# print(users.head())
# Output:
#   Student_ID Student Name  Age Gender  Marks(Out Of 100)  ZIP_Code
# 0           1        Ashis   19      M                 89     85561
# 1           2      Ansuman   32      M                 98     94088
# 2           3   DibyaJyoti   19      M                 96     38344
# 3           4        Borat   19      M                 87     39463
# 4           5    Leepakshi   20      F                 97     72367

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# print(ufo.head())
# ufo['Location']=ufo.City + ','+ufo.State
# print(ufo.head())
# Output:
#                    City Colors Reported Shape Reported State             Time                 Location
# 0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00                Ithaca,NY
# 1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00           Willingboro,NJ
# 2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00               Holyoke,CO
# 3               Abilene             NaN           DISK    KS   6/1/1931 13:00               Abilene,KS
# 4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00  New York Worlds Fair,NY

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# ufo['Location']=ufo.City + ','+ufo.State
# ufo.drop('City',axis=1,inplace=True)
# ufo.drop('State',axis=1,inplace=True)
# print(ufo.head())
# Output:
#   Colors Reported Shape Reported             Time                 Location
# 0             NaN       TRIANGLE   6/1/1930 22:00                Ithaca,NY
# 1             NaN          OTHER  6/30/1930 20:00           Willingboro,NJ
# 2             NaN           OVAL  2/15/1931 14:00               Holyoke,CO
# 3             NaN           DISK   6/1/1931 13:00               Abilene,KS
# 4             NaN          LIGHT  4/18/1933 19:00  New York Worlds Fair,NY

# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head())
# print(movies.describe())
# Output:
#    star_rating                     title content_rating   genre  duration                                        actors_list
# 0          9.3  The Shawshank Redemption              R   Crime       142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2             The Godfather              R   Crime       175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1    The Godfather: Part II              R   Crime       200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0           The Dark Knight          PG-13  Action       152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9              Pulp Fiction              R   Crime       154  [u'John Travolta', u'Uma Thurman', u'Samuel L....   
#        star_rating    duration
# count   979.000000  979.000000
# mean      7.889785  120.979571
# std       0.336069   26.218010
# min       7.400000   64.000000
# 25%       7.600000  102.000000
# 50%       7.800000  117.000000
# 75%       8.100000  134.000000
# max       9.300000  242.000000

# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.shape)
# Output:
# (979, 6)

# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.dtypes)
# Output:
# star_rating       float64
# title              object
# content_rating     object
# genre              object
# duration            int64
# actors_list        object
# dtype: object

# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.describe(include=['object']))
# Output:
#           title content_rating  genre                                        actors_list
# count       979            976    979                                                979
# unique      975             12     16                                                969
# top     Dracula              R  Drama  [u'Daniel Radcliffe', u'Emma Watson', u'Rupert...
# freq          2            460    278                                                  6

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# print(ufo.columns)
# Output:
# Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# ufo.rename(columns={'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'},inplace=True)
# print(ufo.columns)
# Output:
# Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# print(ufo.head())
# ufo.dropna(inplace=True)
# print(ufo.head())
# Output:
#                        City Colors Reported Shape Reported State             Time
# 0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
# 1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
# 2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
# 3               Abilene             NaN           DISK    KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00    
#           City Colors Reported Shape Reported State             Time
# 12      Belton             RED         SPHERE    SC  6/30/1939 20:00
# 19  Bering Sea             RED          OTHER    AK  4/30/1943 23:00
# 36  Portsmouth             RED      FORMATION    VA   7/10/1945 1:30
# 44   Blairsden           GREEN         SPHERE    CA  6/30/1946 19:00
# 82    San Jose            BLUE        CHEVRON    CA  7/15/1947 21:00

# # Wap to find number of rows and coloumns in a uforeports
# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# print(ufo.shape)
# ufo.dropna(inplace=True)
# print(ufo.shape)
# # Output:
# (18241, 5)
# (2486, 5)

# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# ufo.drop('City',axis=1,inplace=True)
# print(ufo.head())
# Output:
#       Colors Reported Shape Reported State             Time
# 0             NaN       TRIANGLE    NY   6/1/1930 22:00
# 1             NaN          OTHER    NJ  6/30/1930 20:00
# 2             NaN           OVAL    CO  2/15/1931 14:00
# 3             NaN           DISK    KS   6/1/1931 13:00
# 4             NaN          LIGHT    NY  4/18/1933 19:00

# Wap to delete multiple coloumns in a uforeports
# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# ufo.drop(['City','State','Time'],axis=1,inplace=True)
# print(ufo.head())
# Output:
#       Colors Reported Shape Reported
# 0             NaN       TRIANGLE
# 1             NaN          OTHER
# 2             NaN           OVAL
# 3             NaN           DISK
# 4             NaN          LIGHT

# Wap to remove multiple rows in a uforeports
# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# ufo.drop([0,1,2,3,4],axis=0,inplace=True)
# print(ufo.head())
# Output:
#               City Colors Reported Shape Reported State              Time
# 5  Valley City             NaN           DISK    ND   9/15/1934 15:30
# 6  Crater Lake             NaN         CIRCLE    CA    6/15/1935 0:00
# 7         Alma             NaN           DISK    MI    7/15/1936 0:00
# 8      Eklutna             NaN          CIGAR    AK  10/15/1936 17:00
# 9      Hubbard             NaN       CYLINDER    OR    6/15/1937 0:00 

# Wap To sort a dataframe on the basis of a particular coloumn in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head())
# print(movies.title.sort_values().head())
# print(movies.title.sort_values(ascending=False).head()) for descending order
# print(movies.sort_values('title').head())
# # Output:
#      star_rating  ...                                        actors_list
# 0          9.3  ...  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2  ...    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1  ...  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0  ...  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9  ...  [u'John Travolta', u'Uma Thurman', u'Samuel L....       

# [5 rows x 6 columns]
# 542     (500) Days of Summer
# 5               12 Angry Men
# 201         12 Years a Slave
# 698                127 Hours
# 110    2001: A Space Odyssey
# Name: title, dtype: object

# 864               [Rec]
# 526                Zulu
# 615          Zombieland
# 677              Zodiac
# 955    Zero Dark Thirty
# Name: title, dtype: object

#      star_rating  ...                                        actors_list     
# 542          7.8  ...  [u'Zooey Deschanel', u'Joseph Gordon-Levitt', ...     
# 5            8.9  ...  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...     
# 201          8.1  ...  [u'Chiwetel Ejiofor', u'Michael Kenneth Willia...     
# 698          7.6  ...  [u'James Franco', u'Amber Tamblyn', u'Kate Mara']     
# 110          8.3  ...  [u'Keir Dullea', u'Gary Lockwood', u'William S..

# Wap to sort a dataframe on the basis of two coloumns in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.sort_values(['star_rating','duration']).head())
# Output:
#          star_rating                title content_rating      genre  duration                                        actors_list
# 938          7.4  Alice in Wonderland              G  Animation        75  [u'Kathryn Beaumont', u'Ed Wynn', u'Richard Ha...
# 948          7.4           Frances Ha              R     Comedy        86  [u'Greta Gerwig', u'Mickey Sumner', u'Adam Dri...
# 966          7.4   The Simpsons Movie          PG-13  Animation        87  [u'Dan Castellaneta', u'Julie Kavner', u'Nancy...
# 947          7.4           Eraserhead        UNRATED      Drama        89  [u'Jack Nance', u'Charlotte Stewart', u'Allen ...
# 971          7.4   Death at a Funeral              R     Comedy        90  [u'Matthew Macfadyen', u'Peter Dinklage', u'Ew...

# Wap to filter rows of a dataframe by coloumn value in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[movies.duration>=200])
# Output:
#        star_rating                                          title  ... duration                                        actors_list
# 0          9.3                       The Shawshank Redemption  ...      142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2                                  The Godfather  ...      175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0                                The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9                                   Pulp Fiction  ...      154  [u'John Travolta', u'Uma Thurman', u'Samuel L....
# 5          8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 6          8.9                 The Good, the Bad and the Ugly  ...      161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...
# 7          8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 8          8.9                               Schindler's List  ...      195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...
# 9          8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...

# [10 rows x 6 columns]
#      star_rating                                          title  ... duration                                        actors_list        
# 2            9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...        
# 7            8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...        
# 17           8.7                                  Seven Samurai  ...      207  [u'Toshir\xf4 Mifune', u'Takashi Shimura', u'K...        
# 78           8.4                    Once Upon a Time in America  ...      229  [u'Robert De Niro', u'James Woods', u'Elizabet...        
# 85           8.4                             Lawrence of Arabia  ...      216  [u"Peter O'Toole", u'Alec Guinness', u'Anthony...        
# 142          8.3              Lagaan: Once Upon a Time in India  ...      224  [u'Aamir Khan', u'Gracy Singh', u'Rachel Shell...        
# 157          8.2                             Gone with the Wind  ...      238  [u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...        
# 204          8.1                                        Ben-Hur  ...      212  [u'Charlton Heston', u'Jack Hawkins', u'Stephe...        
# 445          7.9                           The Ten Commandments  ...      220  [u'Charlton Heston', u'Yul Brynner', u'Anne Ba...        
# 476          7.8                                         Hamlet  ...      242  [u'Kenneth Branagh', u'Julie Christie', u'Dere...        
# 630          7.7                                      Malcolm X  ...      202  [u'Denzel Washington', u'Angela Bassett', u'De...        
# 767          7.6                It's a Mad, Mad, Mad, Mad World  ...      205  [u'Spencer Tracy', u'Milton Berle', u'Ethel Me...

# WAP to filter rows of a dataframe by coloumn value in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[movies.duration>=200].genre)
# # Or print(movies.loc[movies.duration>=200,'genre'])
# Output:
#        star_rating                                          title  ... duration                                        actors_list
# 0          9.3                       The Shawshank Redemption  ...      142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2                                  The Godfather  ...      175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0                                The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9                                   Pulp Fiction  ...      154  [u'John Travolta', u'Uma Thurman', u'Samuel L....
# 5          8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 6          8.9                 The Good, the Bad and the Ugly  ...      161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...
# 7          8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 8          8.9                               Schindler's List  ...      195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...
# 9          8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...

# [10 rows x 6 columns]
# 2          Crime
# 7      Adventure
# 17         Drama
# 78         Crime
# 85     Adventure
# 142    Adventure
# 157        Drama
# 204    Adventure
# 445    Adventure
# 476        Drama
# 630    Biography
# 767       Action
# Name: genre, dtype: object

# WAP to demonstrate logiccal operator in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[(movies.duration>=200) & (movies.genre=='Drama')])
# Output:
#     star_rating                                          title  ... duration                                        actors_list
# 0          9.3                       The Shawshank Redemption  ...      142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2                                  The Godfather  ...      175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0                                The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9                                   Pulp Fiction  ...      154  [u'John Travolta', u'Uma Thurman', u'Samuel L....
# 5          8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 6          8.9                 The Good, the Bad and the Ugly  ...      161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...
# 7          8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 8          8.9                               Schindler's List  ...      195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...
# 9          8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...

# [10 rows x 6 columns]
#      star_rating               title content_rating  genre  duration                                        actors_list
# 17           8.7       Seven Samurai        UNRATED  Drama       207  [u'Toshir\xf4 Mifune', u'Takashi Shimura', u'K...
# 157          8.2  Gone with the Wind              G  Drama       238  [u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...
# 476          7.8              Hamlet          PG-13  Drama       242  [u'Kenneth Branagh', u'Julie Christie', u'Dere...

# WAP to demonstrate logical or operator in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[(movies.duration>=200) | (movies.genre=='Drama')].head())
# OutPut:
#      star_rating                                          title  ... duration                                        actors_list
# 0          9.3                       The Shawshank Redemption  ...      142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2                                  The Godfather  ...      175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0                                The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9                                   Pulp Fiction  ...      154  [u'John Travolta', u'Uma Thurman', u'Samuel L....
# 5          8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 6          8.9                 The Good, the Bad and the Ugly  ...      161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...
# 7          8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 8          8.9                               Schindler's List  ...      195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...
# 9          8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...

# [10 rows x 6 columns]
#     star_rating                                          title  ... duration                                        actors_list
# 2           9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 5           8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 7           8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 9           8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...
# 13          8.8                                   Forrest Gump  ...      142    [u'Tom Hanks', u'Robin Wright', u'Gary Sinise']

# WAP to demonstrate logical multiple or operator in a imdb
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[(movies.duration>=200) | (movies.genre=='Drama') | (movies.genre=='Crime')].head())
# Or movies[movies.genre.isin(['Drama','Crime','Action'])].head()]

# WAP to when reading from a file how do read in only a subset of the columns by coloumn name
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings')
# print(movies.head(10))
# print(movies[['title','genre','content_rating','duration']].head())

# # WAP to when reading from a file how do read in only a subset of the columns by coloumn position
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings',usecols=[0,1,2,3,4])
# print(movies.head(10))

# Output:
#        star_rating                                          title  ... duration                                        actors_list
# 0          9.3                       The Shawshank Redemption  ...      142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1          9.2                                  The Godfather  ...      175    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2          9.1                         The Godfather: Part II  ...      200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3          9.0                                The Dark Knight  ...      152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4          8.9                                   Pulp Fiction  ...      154  [u'John Travolta', u'Uma Thurman', u'Samuel L....
# 5          8.9                                   12 Angry Men  ...       96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 6          8.9                 The Good, the Bad and the Ugly  ...      161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...
# 7          8.9  The Lord of the Rings: The Return of the King  ...      201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...
# 8          8.9                               Schindler's List  ...      195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...
# 9          8.9                                     Fight Club  ...      139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...

# [10 rows x 6 columns]
#                       title   genre content_rating  duration
# 0  The Shawshank Redemption   Crime              R       142
# 1             The Godfather   Crime              R       175
# 2    The Godfather: Part II   Crime              R       200
# 3           The Dark Knight  Action          PG-13       152
# 4              Pulp Fiction   Crime              R       154
#    star_rating                                          title content_rating      genre  duration
# 0          9.3                       The Shawshank Redemption              R      Crime       142
# 1          9.2                                  The Godfather              R      Crime       175
# 2          9.1                         The Godfather: Part II              R      Crime       200
# 3          9.0                                The Dark Knight          PG-13     Action       152
# 4          8.9                                   Pulp Fiction              R      Crime       154
# 5          8.9                                   12 Angry Men      NOT RATED      Drama        96
# 6          8.9                 The Good, the Bad and the Ugly      NOT RATED    Western       161
# 7          8.9  The Lord of the Rings: The Return of the King          PG-13  Adventure       201
# 8          8.9                               Schindler's List              R  Biography       195
# 9          8.9                                     Fight Club              R      Drama       139

# WAP to when reading from a file how do read in only a subset of the rows by row position
# import pandas as pd
# movies=pd.read_csv('http://bit.ly/imdbratings',nrows=5)
# print(movies.head())

# WAP to iterate through a series in a uforeports
# import pandas as pd
# ufo=pd.read_csv('http://bit.ly/uforeports')
# for index,row in ufo.iterrows():
#     print(row['City'],row['State'])

# WAP to drop all non-numeric coloumns in a drinkbycountry
# import pandas as pd
# import numpy as np
# drinks=pd.read_csv('http://bit.ly/drinksbycountry')
# print(drinks.dtypes)
# drinks=drinks.select_dtypes(include=[np.number])
# print(drinks.head())
# Output:
#     country                          object
# beer_servings                     int64
# spirit_servings                   int64
# wine_servings                     int64
# total_litres_of_pure_alcohol    float64
# continent                        object
# dtype: object
#    beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# 0              0                0              0                           0.0
# 1             89              132             54                           4.9
# 2             25                0             14                           0.7
# 3            245              138            312                          12.4
# 4            217               57             45                           5.9

# WAP to use Describe function in a drinkbycountry
# import pandas as pd
# drinks=pd.read_csv('http://bit.ly/drinksbycountry')
# print(drinks.describe())
# print(drinks.describe(include='all'))
# print(drinks.describe(include=['object','float64']))
# Output:
#            beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# count     193.000000       193.000000     193.000000                    193.000000
# mean      106.160622        80.994819      49.450777                      4.717098
# std       101.143103        88.284312      79.697598                      3.773298
# min         0.000000         0.000000       0.000000                      0.000000
# 25%        20.000000         4.000000       1.000000                      1.300000
# 50%        76.000000        56.000000       8.000000                      4.200000
# 75%       188.000000       128.000000      59.000000                      7.200000
# max       376.000000       438.000000     370.000000                     14.400000
#             country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# count           193     193.000000       193.000000     193.000000                    193.000000       193
# unique          193            NaN              NaN            NaN                           NaN         6
# top     Afghanistan            NaN              NaN            NaN                           NaN    Africa
# freq              1            NaN              NaN            NaN                           NaN        53
# mean            NaN     106.160622        80.994819      49.450777                      4.717098       NaN
# std             NaN     101.143103        88.284312      79.697598                      3.773298       NaN
# min             NaN       0.000000         0.000000       0.000000                      0.000000       NaN
# 25%             NaN      20.000000         4.000000       1.000000                      1.300000       NaN
# 50%             NaN      76.000000        56.000000       8.000000                      4.200000       NaN
# 75%             NaN     188.000000       128.000000      59.000000                      7.200000       NaN
# max             NaN     376.000000       438.000000     370.000000                     14.400000       NaN
#             country  total_litres_of_pure_alcohol continent
# count           193                    193.000000       193
# unique          193                           NaN         6
# top     Afghanistan                           NaN    Africa
# freq              1                           NaN        53
# mean            NaN                      4.717098       NaN
# std             NaN                      3.773298       NaN
# min             NaN                      0.000000       NaN
# 25%             NaN                      1.300000       NaN
# 50%             NaN                      4.200000       NaN
# 75%             NaN                      7.200000       NaN
# max             NaN                     14.400000       NaN

