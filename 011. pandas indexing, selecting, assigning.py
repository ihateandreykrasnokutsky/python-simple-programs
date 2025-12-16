import pandas as pd

wow_data=pd.read_csv("./python-simple-programs/011. wow_data.csv")
print ("WOW DATA:")
print (wow_data)
print ("ILOC")
print (wow_data.iloc[[0,5,7],0])
print ("ILOC MINUS")
print (wow_data.iloc[[-1],0])
print ("LOC")
print ("Victory for ", wow_data.loc[3,"Participant"],'.')
print ("LOC WITH STRING INDICES")
print (wow_data.loc[:,["Doomhammer Replica", "Arcane Staff of Quel'Thalas"]])
#next is "Choosing between loc and iloc", https://www.kaggle.com/code/residentmario/indexing-selecting-assigning


