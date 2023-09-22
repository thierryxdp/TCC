def qtd_divisores(n):
    ''' funcao que dado um numero n retorna a sua quantidade de divisores
    int-> int'''
    soma = 0
    for i in range(1, n+1):
        if n % i == 0 :
            soma = soma + 1
        else:
            continue 
    return soma