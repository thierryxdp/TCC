#QUESTAO6
def faltante(lista):
    '''
    Retorna qual a peça do quebra-cabeça
    esta faltando.
    list -> int
    '''
    
    lista.sort()
    indice = 0
    while indice < len(lista):
        if indice+1 != lista[indice]:
            return indice+1    
        indice = indice+1
    return len(lista)+1