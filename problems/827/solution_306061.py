def qtd_divisores(n:int)->int:
    '''retorna a quantidade de divisores que um número (n) tem'''
    resultado = 0
    for numero in range(1,n):
        if(n % numero) == 0:
            resultado = resultado + 1
    return resultado