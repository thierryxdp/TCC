def faltante(lista):
    '''funcao que retorna valor do item faltante da sequencia da lista de entrada.
    list(int) -> int'''
    indice = 0
    while lista[indice]+1==lista[indice+1]:
        indice=indice+1
    return lista[indice]+1