import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,8))

x_us=[0,1,1,0,0]
y_us=[0,0,1,1,0]

x_Rus=[0,0.71,0,-0.71,0]
y_Rus=[0,0.71,1.42,0.71,0]
x_Bus=[0,1,2,1,0]
y_Bus=[0,0,1,1,0]

x_BRus=[0,1.42,1.42,0,0]
y_BRus=[0,0.71,1.42,0.71,0]
x_RBus=[0,0.71,0.71,0,0]
y_RBus=[0,0.71,2.13,1.42,0]

plt.plot(x_us,y_us,linewidth=5,color='dimgray',label='unit square (us)')
plt.plot(x_Rus,y_Rus,linewidth=3,color='red',label='rotation')
plt.plot(x_BRus,y_BRus,linewidth=3,color='darkred',label='rotation=>shear')
plt.plot(x_Bus,y_Bus,linewidth=2,color='green',label='shear')
plt.plot(x_RBus,y_RBus,linewidth=2,color='darkgreen',label='shear=>rotation')

plt.grid(True,alpha=1)
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Non-Commutativity of Linear Transformations')
plt.legend()
plt.show()