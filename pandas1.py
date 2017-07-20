#trial code 

import pandas as pd
import numpy as np

dict = {
    "country":["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":["Rio", "Moscow", "Delhi","Beijing","Pretoria"],
    "area":["8.516","17.10","3.286","9.597","1.221"],
    "population":[200.4, 100.6, 99.5, 78.6, 88.0]
    }

print (dict)

brics = pd.DataFrame(dict)
print (brics)

#brics.index['BR','RU','IN','CH','SA']
#print (brics)
