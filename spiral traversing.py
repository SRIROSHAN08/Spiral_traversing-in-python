a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
       l.append(count)
       count=count+1
    a.append(l)



#######################
#####Matrix spiral#####
#######################

def spiral(m,n,a):
    # m-> row  index(max)
    # n-> column index(max)
    # a-> Matrix(n X n)
    
    k=0
    l=0
    
    # k-> starting index of m
    # l-> starting index of n
    while (k<m and l<n  ):
        #Printing the first row from the remaining row
        for i in range(l,n):
            print(a[k][i], end=" ")
        
        k=k+1
        #priniting the last column from the remaining column
        for i in range(k,m):
            print(a[i][n-1], end=" ")
            
        n=n-1
        #printing the last row from the remaining row
        if k<m:
            for i in range(n-1,l-1,-1):
                print(a[m-1][i], end=" ")
        m=m-1
        #printing the first column from the remaining column
        if l<n:
             for i in range(m-1,k-1,-1):
                 print(a[i][l], end=" ")
        l=l+1



