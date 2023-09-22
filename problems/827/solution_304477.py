def qtd_divisores(n):
    divisores = 0
    for divisao in range(1,n+1):
        if n % divisao == 0:
        divisao +=1
    return len(divisao)
        else:
            lista2 = n//divisores
        return lista2