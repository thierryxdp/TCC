def soma_h(n):
    return round(sum([(1/x) for x in range(1, n + 1)]), 2)
    num = int(input('8: '))
     print(soma_h(num))