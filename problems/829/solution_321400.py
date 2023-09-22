def soma_h(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return round(1/num,2)