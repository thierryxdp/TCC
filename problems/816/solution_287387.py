def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma lista
    maiores que n
    list -> list'''
    
    lista_final = []
    
    for elemento in lista:
        if elemento > n:
            return lista_final.append(elemento)