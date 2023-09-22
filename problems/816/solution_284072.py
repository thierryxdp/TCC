def maiores (lista, n):
    '''funcao que retorna uma lista com numeros maiores que n'''
    lista_final = lista
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            return lista_final