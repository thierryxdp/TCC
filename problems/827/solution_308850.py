def qtd_divisores(num):
    
    result = 0
    for d in range(num(+1)):
        if num%d == 0:
            result += 1
    return result