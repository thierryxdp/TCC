def qtd_divisores (x):
    'recebe um numero e conta quantos divisores  ele possui'
    'entrada: int'
    'saida: int'
    divisores=0
    for a in range(1,n+1):
        if x%a==0:
            divisores+=1
    return divisores