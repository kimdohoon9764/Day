#두개의 행렬 A,B를 직접 곱해보고 ,코드로 검산하기

#A=2x3행렬 B=3x2행렬
A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]

C=[]
tmp=[]
row=0
col=0
for i in range(len(A)):
    for j in range(len(A[0])):
        tmp[i]=A[i][j]*B[j][i]
    
print(tmp)