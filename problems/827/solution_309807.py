def qtd_divisores(num):
    total = 0
    for div in range(num+1):
        if div != 0:
            if num%div == 0:
                total+=1
    return total