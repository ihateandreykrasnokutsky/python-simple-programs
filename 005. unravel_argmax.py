import numpy as np
array=np.random.randint(low=0,high=9,size=(3,3)) #generate random number
argmax=np.argmax(array) #find an index of the flattened initial array's maximum number
index=np.unravel_index(np.argmax(array), array.shape) #find what the argmax corresponds to in a not 1D array
print (f"array=\n{array}")
print (f"argmax={argmax}")
print (f"index={index}")