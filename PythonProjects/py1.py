# # import pandas as pd 
# # calories = {"day1": 420, "day2": 380, "day3": 390} 
# # myvar = pd.Series(calories) 
# # print(myvar) 

# import pandas as pd 
# data = pd.Series((0.25, 0.5, 0.75, 1.0)) 
# print(data.values) 
# print(data.index) 
# print(data.keys) 

# import pandas as pd 
# data = pd.Series((3,6,9,8,5,4,2,6,3,5,8)) 
# print(data.describe()) 

# import pandas as pd  
# data = {"calories": [420, 380, 390],"duration": [50, 40, 45]} 
# df = pd.DataFrame(data) 
# print(df) 

# print(df.loc[0]) 
# print(df['duration']) 

import pandas as pd 
import numpy as np 
df = pd.DataFrame(np.random.randint(3,10 ,(5,3)), 
columns=['A', 'B', 'C']) 
result = df.query('A < 0.5 and B < 0.5') 
print(df) 
print(result) 



