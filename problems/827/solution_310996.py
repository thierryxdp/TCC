def qtd_divisores(x):
    if x<=0:
        return 0
    divisores = [x]
    for i in range(1, x//2+1):
        if x % i == 0:
            divisores.append(i)
    return len(divisores)