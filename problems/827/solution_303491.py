def qtd_divisores(n):
    """retorna a quantidade de divisores do numero de entrads n"""
    soma = 0
    if n <=0:
        return 0
    else:
        for i in range(1, n//2+1):
            if n % i == 0:
                soma = soma + 1
        return soma + 1