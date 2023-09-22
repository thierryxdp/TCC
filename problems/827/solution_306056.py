def qtd_divisores(n:int)->int:
    '''retorna a quantidade de divisores que um número (n) tem'''
    resultado = 0
    for numero in range(n):
        if numero % n == 0:
            resultado += 1
    return resultado