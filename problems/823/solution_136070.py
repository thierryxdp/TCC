def faltante(lista):
    '''funcao que retorna valor do item faltante da sequencia da lista de entrada.
    list(int) -> int'''
    indice = 0
    contador = 1
    if lista[0] != 1:
        return 1
    while contador<len(lista):
        while lista[indice]+1==lista[indice+1]:
            indice=indice+1
            contador=contador+1
      
    return lista[indice]+1