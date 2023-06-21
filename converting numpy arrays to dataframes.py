import numpy as np
import pandas as pd

arr = np.random.rand(3) #to create an one dimensional array
print("Numpy array:")
print(arr)

#conversion of array to series
series = pd.Series(arr)
print("Series : ")
print(series)

# conversion of series to dataframe
df = pd.DataFrame(series,columns =['A'])
print("\nSeries to DataFrame: ")
print(df)
