def qtd_divisores(num):
    i = 0
    for elemento in range(1,num):
        if num%elemento == 0:
            i = i + 1
    if num >=0:
        return i
    else:
        return i + 1