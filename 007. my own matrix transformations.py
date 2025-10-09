import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,8))

x1=[0,1,1,0,0]
y1=[0,0,1,1,0]
x2=[0,5,28,23,0]
y2=[0,25,68,43,0]
x3=[0,209,362,153,0]
y3=[0,369,702,333,0]

plt.plot(x1,y1,linewidth=5,color='red',label='Unit Square')
plt.plot(x2,y2,linewidth=2,color='blue',label='Unit Square 2')
plt.plot(x3,y3,linewidth=1,color='green',label='Unit Square 3')

plt.grid(True,alpha=1)
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('my own matrix transformations')
plt.legend()
plt.show()


