def faltante(lista):
    '''funcao que retorna valor do item faltante da sequencia da lista de entrada.
    list(int) -> int'''
    indice = 1
    while indice<len(lista):
        if indice in lista:
            indice=indice+1
       
    return lista[indice-1]+1