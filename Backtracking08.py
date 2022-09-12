def is_attack(i,j,b,N):
    for k in range(1,i):
        if(b[k][j] == 1):
          return True
    k = i-1
    l = j+1
    while(k>=1 and l<=N):
      if(b[k][l] == 1):
        return True
      k = k+1
      l = l+1
    k = i-1
    l = j-1
    while(k>=1 and l>=1):
      if(b[k][l] == 1):
        return True
      k = k-1
      l = l-1
    return False

def n_queen(r,n,N,b):
    if (n == 0):
       return True
    for j in range(1,N+1):
        if(not(is_attack(r,j,b,N))):
          b[r][j] = 1
          if(n_queen(r+1,n-1,N,b)): # bug hocchilo
            return True
          b[r][j] = 0
    return False


b = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
n_queen(1,4,4,b)
for i in range(1,5):
    print(b[i][1:])
