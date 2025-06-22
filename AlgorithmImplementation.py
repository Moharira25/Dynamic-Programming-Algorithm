def minCost(n, S, K, C, d):
    cost = [[float('inf') for _ in range(S + 1)] for _ in range(n + 1)]
    cost[0][0] = 0
 
    prevStorages = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
 
    for i in range(1, n+1):
        for j in range(S + 1):
            for s in range(S +1):
                orderSize = max(0, d[i-1] + j - s)
                orderCost = K if orderSize > 0 else 0
 
                if cost[i-1][s] != float('inf'):
                    totalCost = cost[i-1][s] + orderCost + j * C
 
                    if totalCost < cost[i][j]:
                        cost[i][j] = totalCost
                        prevStorages[i][j] = s
 
    return cost[n][0], prevStorages, cost
 
def traceback(n, d, prevStorages):
    orders = [0] * n
    j = 0
    for i in range(n,0,-1):
        prevInventory = prevStorages[i][j]
        orders[i-1] = max(0, d[i-1] + j - prevInventory)
        j = prevInventory
    
    return orders
 
S = 5
C = 1
K = 4
n = 5
demands = [6, 2, 1, 1, 6]
 
min_cost, prevStorages, dp = minCost(n, S, K, C, demands)
 
print("Min Cost: " + str(min_cost))
print("\nDp:")
for r in dp:
    print(r)
 
orders = traceback(n,demands, prevStorages)
print("\nTraceback: " )
for b in prevStorages:
    print(b)
print("\nOrders:")
print(orders)
