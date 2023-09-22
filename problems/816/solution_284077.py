def maiores (lista, n):
    '''funcao que retorna uma lista com numeros maiores que n'''
    for elemento in lista:
        if elemento > n:
            lista.append(elemento)
            return lista