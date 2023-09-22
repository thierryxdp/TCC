def faltante(L):
    '''Função que retorna a peça que está faltando no quebra-cabeças de entrada: list -> int'''
    L.sort()
    indice = 1
    while indice in L:
        indice += 1 #indice = indice + 1
    return indice