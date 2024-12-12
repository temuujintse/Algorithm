
def Prime_number(n):
    memo ={}

    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            memo[n] = False
            return False
        memo[n] = True
        return True
    
def Print_P(n):
    for num in range(1, n+1):
        if Prime_number(num):
            print(num)

Print_P(18)