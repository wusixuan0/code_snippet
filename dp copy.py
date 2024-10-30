import sys
  def knapsack(self, capacity, weight, value):
    n = len(weight)
    dp = [[0]*(capacity+1) for i in range(n+1)]

    for i in range(n+1):
      for j in range(capacity+1):
        if i == 0 or j == 0:
          dp[i][j] = 0
        elif weight[i-1] > j:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+ value[i-1])
    return dp[n][capacity]
    
def findStep(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
 
    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
 

n = int(sys.argv[1])
print(findStep(n))

