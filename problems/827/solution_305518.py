def qtd_divisores(n):
    '''Função retorna, dado um numero, quantos divisores esse termo possui
    int -> int'''
    quantos = 0
    for a in range(1, n+1):
        if n%a==0:
            quantos += 1
            
    return quantos