def faltante(lista):
    '''Retorna o numero que esta faltando em uma lista em forma de sequencia
       parameters:
       lista: lista original com elementos em sequencia
       list->int'''
    proximo=1
    while proximo in lista:
        proximo=proximo+1
    return proximo