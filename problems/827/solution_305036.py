def qtd_divisores(n):
    '''retorna quantos divisores o numero n possui; int -> int'''
    soma=0
    for (numero in range(n)) and !=0:
        if n%numero==0:
            soma=soma+1
    return soma