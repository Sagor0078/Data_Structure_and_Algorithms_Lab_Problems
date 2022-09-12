# 01 knapsack 
#  first notice that we are dealing with 2 dimensions; the first one is just an index for the items, 
#and the second one is the capacity we are dealing with right now.
# retrieve the answer, just take max(dp[w]) between all valid w.
def knapsack(p,wt,C,n):
     dp = [0 for i in range(C+1)]
     for i in range(1,n+1):
         for w in range(C,0,-1): # starting from the back 
              if wt[i-1] <= w:   # if(w - wt[i] >= 0)
                 dp[w] = max(dp[w], dp[w-wt[i-1]] + p[i-1])
                #  print(dp[w])
     return dp[C]

p = [15,25,13,23]
wt = [2,6,12,9]
C = 20
n = len(p)
# knapsack(p,wt,C,n)
print(knapsack(p,wt,C,n))
