def soma_h(n):
    num = 1
    div = 0
    for i in range(1,n+1):
        num *= i
        div += i

    return round(num/div,2)