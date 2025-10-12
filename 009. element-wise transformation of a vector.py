import matplotlib.pyplot as plt
import numpy as np
import random
plt.figure(figsize=(10,8))

vector1=(1,1)
vector2=(-1,0.5)
plt.quiver(0,0,vector1[0],vector1[1],angles='xy',scale_units='xy',scale=1,color='black',label='vector1',width=0.005)
plt.quiver(0,0,vector2[0],vector2[1],angles='xy',scale_units='xy',scale=1,color='red',label='vector2',width=0.005)
for i in range(1):
    scalex=random.randrange(-9,9)
    scaley=random.randrange(-9,9)
    randcolor1=random.random()
    randcolor2=random.random()
    randcolor3=random.random()
    vector1a=(vector1[0]*scalex,vector1[1]*scaley)
    vector2a=(vector2[0]*scalex,vector2[1]*scaley)
    plt.quiver(0,0,vector1a[0],vector1a[1],angles='xy',scale_units='xy',scale=1,color='blue',label=f'vector1a{i}',width=0.003) #(randcolor1,randcolor2,randcolor3)
    plt.quiver(0,0,vector2a[0],vector2a[1],angles='xy',scale_units='xy',scale=1,color='green',label=f'vector2a{i}',width=0.003)

plt.grid(True,alpha=1)
plt.axhline(y=0,color='k',linewidth=2)
plt.axvline(x=0,color='k',linewidth=2)
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('element-wise 1D multiplication instead of 2D matrix multiplication')
plt.legend()
plt.show()