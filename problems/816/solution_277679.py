def maiores(lista, n):
    ''' funcao que dada uma lista de numeros int e um numero n, retorna uma lista que contenha os numeros maiores que n'''
     lista_retorno = []
    for elemento in lista:
        if elemento > n:
            lista_retorno.append(elemento)  
    lista_retorno.sort()
    return lista_retorno