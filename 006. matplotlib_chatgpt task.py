import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,8))
square_x=[0,1,1,0,0]
square_y=[0,0,1,1,0]
square_x_stretched=[0,2,2,0,0]
square_y_strethced=[0,0,1,1,0]
square_x_sheared=[0,0,1,1,0]
square_y_sheared=[0,1,2,1,0]
square_x_rotated=[0,0.71,0,-0.71,0]
square_y_rotated=[0,0.71,1.42,0.71,0]
square_x_reflected=[0,1,1,0,0]
square_y_reflected=[0,0,-1,-1,0]
plt.plot(square_x,square_y,linewidth=8,color='red',label='Unit Square')
plt.plot(square_x_stretched,square_y_strethced,linewidth=6,color='purple',label='Stretched')
plt.plot(square_x_sheared,square_y_sheared,linewidth=4,color='green',label='Sheared')
plt.plot(square_x_rotated,square_y_rotated,linewidth=3,color='pink',label='Rotated')
plt.plot(square_x_reflected,square_y_reflected,linewidth=2,color='royalblue',label='Reflected')

plt.grid(True,alpha=1)
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('ChatGPT task to understand matrices as transformations')
plt.legend()
plt.show()