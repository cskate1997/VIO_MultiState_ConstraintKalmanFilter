import math
def func(arr):
    n = len(arr)

    pre = n * [0]
    dp = n * [0]
    pre[0] = arr[0]
    dp[0] = arr[0]

    for i in range(1,n):
        pre[i] = pre[i-1] + arr[i]

    for i in range(1,n):
        if arr[i]<= dp[i-1]:
            dp[i] = dp[i-1]

        else:
            dp[i] = max(dp[i-1], math.ceil(pre[i] / (i+1)))

    return dp[n - 1]
