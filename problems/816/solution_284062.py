def maiores (lista, n):
    '''funcao que retorna uma lista com numeros maiores que n'''
    lista = [0,2,3]
    n = 1
    lista_final = []
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            return lista_final