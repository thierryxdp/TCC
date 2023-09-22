def qtd_divisores(n):
    '''Função que retorna o número de divisores que "n"possui de entrada: int -> int'''
    
    numero = n
    lista = []
    
    for indice in range(1, n+1):
        if numero % indice == 0:
            lista.append(indice)
    return len(lista)