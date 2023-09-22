def faltante(lista):
    '''funcao que retorna valor do item faltante da sequencia da lista de entrada.
    list(int) -> int'''
    indice = 1
    contador = 0
    while indice<=(len(lista)+1):
        while indice<len(lista):
            if lista[contador]==indice:
            	contador=contador+1
            	indice=indice+1
            else:
                return indice