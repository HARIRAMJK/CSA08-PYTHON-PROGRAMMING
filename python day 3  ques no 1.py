def findMaxProfit(price):
 
    n = len(price)
 
    # base case
    if n == 0:
        return 0
 
    
    profit = [0] * n
 
    profit[n - 1] = 0
 
    
    max_so_far = price[n - 1]
 
    
    for i in reversed(range(n - 1)):
 
        
        
        profit[i] = max(profit[i + 1], max_so_far - price[i])
 
        
        max_so_far = max(max_so_far, price[i])
 
    min_so_far = price[0]

    
    
    for i in range(1, n):
 
        ''' Update profit[i] by taking a maximum of the following:
           1. profit[i-1], which represents the maximum profit calculated so far
           2. The total profit obtained by closing the first transaction on the day `i`
              and performing another transaction from the day `i` till day `n-1`. '''
 
        profit[i] = max(profit[i - 1], (price[i] - min_so_far) + profit[i])
 
        
        min_so_far = min(min_so_far, price[i])
 
    
    return profit[n - 1]
 
 
if _name_ == '_main_':
 
    price = [2, 4, 7, 5, 4, 3, 5]
 
    print('The maximum profit is', findMaxProfit(price))
 
