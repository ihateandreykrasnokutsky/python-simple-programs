import pandas as pd

data_wow=pd.DataFrame({
    'Name': ['Arthas', 'Jaina', 'Thrall'],
    'Class': ['Death Knight', 'Mage', 'Shaman'],
    'Level': [80, 85, 90],
    'Health': [5000, 3000, 4500]
})
data_wow=data_wow.set_index("Class")
print (data_wow.iloc[:,:])

print ("NUMBER DATA FRAME")
ndf=pd.DataFrame({
    1:[34,53],
    2:[32,55],
    3:[12,93],
    4:[56,23],
})
ndf=ndf.set_index(4)
print (ndf)