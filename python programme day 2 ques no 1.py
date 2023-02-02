def staircase(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
 
    else:
        return staircase(n - 2) + staircase(n - 1)
n = 5
print(staircase(n))
