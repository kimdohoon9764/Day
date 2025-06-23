import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
relu=np.maximum(0,x)
drelu=(np.where(x>0,1,0))

plt.plot(x,relu,label='ReLU')
plt.plot(x,drelu,label="ReLU'")
plt.legend()
plt.grid()
plt.show()