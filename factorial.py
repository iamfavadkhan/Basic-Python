print("Try programiz.pro")
def fact(n):
    if n == 0:
        return 1
    
    return n*fact(n-1)
        
print(fact(6))

# 5 * (n-1)
# 5 * 4 (n-1)
# 5 * 4 * 3 (n-1)
# 5 * 4 * 3 * 2 (n-1)
# 5 * 4 * 3 * 2  * 1
