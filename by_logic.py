def show(l1):
    for i in l1:
        for j in i:
            print(j,end="    ")
        print()

def input_matrix(matrix):
    for i in range(n):
        for j in range(n):
            x=int(input())
            matrix[i][j]=x
    return matrix

n=int(input("Enter the rows and columns:  "))
matrix=[["-"]*n for i in range(n)]
(show(matrix))
print("Enter the elements: ")
matrix=input_matrix(matrix)
print("\n\n\nMatrix:     \n")
show(matrix)

l=[]
for i in range(2,n+1):
    l.append(i)

p=[]
from itertools import permutations 
pern=permutations(l)
for i in (pern):
    p.append(list(i))

for (i) in (p):
    i.insert(0,1)
    (i).append(1)
print("\n\n\nNumber of possible paths :   ")
show(p)

sum1=0
sums=[]
d1={}
for i in p:
    a=1
    sum1=0
    for j in i:
        sum1=sum1+(matrix[a-1][j-1])
        a=j
    d1[sum1]=i
    sums.append(sum1)

print("\n\n\n",d1)
ans=(min(d1.keys()))

print("\n\nMinimum cost of all the path: ",ans)
print("\nPath:  ",d1[ans])
