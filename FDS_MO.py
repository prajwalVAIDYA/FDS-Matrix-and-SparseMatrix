print("Matrix Size :")
r=int(input("Enter Number of Rows : "))
c=int(input("Enter Number of Columns  : "))
print("\n")
print("Matrix 1 Elements")
m1=[]
for i in range (r):
  a=[]
  for j in range (c):
    a.append(int(input("Enter Elements : ")))
  m1.append(a)
for i in range(r):
  for j in range (c):
    print(m1[i][j],end=" ")
  print()
print("\n")
print("Matrix 2 Elements")
m2=[]
for i in range (r):
  a=[]
  for j in range (c):
    a.append(int(input("Enter Elements : ")))
  m2.append(a)
for i in range(r):
  for j in range (c):
    print(m2[i][j],end=" ")
  print()
print("\n")

# Adding M1 and M2
print("New Matrix showing Addition of M1 and M2\n")
add=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m1[0])):
       add[i][j] = m1[i][j] + m2[i][j]
for k in add:
   print(k)
print("\n")

# Subtracting M1 and M2
print("New Matrix showing Subtracting of M1 and M2\n")
sub=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m1[0])):
       sub[i][j] = m1[i][j] - m2[i][j]
for k in sub:
   print(k) 
print("\n")

#Multiplying M1 and M2
print("New Matrix showing Multiplication of M1 and M2\n")
mul=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m2[0])):
     for k in range(len(m2)):
       mul[i][j] += m1[i][k] * m2[k][j]
for k in mul:
   print(k)
print("\n")

# Transpose of M1 and M2
print("New Matrix showing Transpose of M1")
trans1=[[0 for i in range (c)]for j in range (r)]
for i in range (len(m1)):
  for j in range (len(m1[0])):
    trans1[j][i]=m1[i][j]
for k in trans1:
  print(k)
print("\n")

print("New Matrix showing Transpose of M2")
trans2=[[0 for i in range (c)]for j in range (r)]
for i in range (len(m2)):
  for j in range (len(m2[0])):
    trans2[i][j]=m2[j][i]
for k in trans2:
  print(k)
print("\n")



#Output


#Matrix Size :
#Enter Number of Rows : 2
#Enter Number of Columns  : 2


#Matrix 1 Elements
#Enter Elements : 3
#Enter Elements : 2
#Enter Elements : 3
#Enter Elements : 2
#3 2 
#3 2 


#Matrix 2 Elements
#Enter Elements : 2
#Enter Elements : 1
#Enter Elements : 2
#Enter Elements : 1
#2 1 
#2 1 


#New Matrix showing Addition of M1 and M2

#[5, 3]
#[5, 3]


#New Matrix showing Subtracting of M1 and M2

#[1, 1]
#[1, 1]


#New Matrix showing Multiplication of M1 and M2

#[10, 5]
#[10, 5]


#New Matrix showing Transpose of M1
#[3, 3]
#[2, 2]


#New Matrix showing Transpose of M2
#[2, 2]
#[1, 1]
