import numpy as np
import matplotlib.pyplot as plt


def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))\
        
        
A=np.array([1,0])
B=np.array([0,1])
C=np.array([1,1])


plt.quiver(0,0,A[0],A[1],angles="xy",scale_units="xy",scale=1,color='r',label='A')
plt.quiver(0,0,B[0],B[1],angles='xy',scale_units='xy',scale=1,color='b',label='B')
plt.quiver(0,0,C[0],C[1],angles='xy',scale_units='xy',scale=1,color='g',label="C")
plt.xlim(-1,2)
plt.ylim(-1,2)
plt.grid()
plt.legend()
plt.show()


print("A•B = ",np.dot(A,B))
print("A * B.T =",np.matmul(A,B.T))
print("cos(A,C) =", cosine_similarity(A,C))