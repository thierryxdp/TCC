def faltante (lista):
    """Retorna a peça faltante do quebra-cabeça do Joãozinho; lista -> int"""
    listareal = []
    i = 0
    while i<len(lista)+1:
        listareal = listareal + [i+1,]
        i=i+1
    return sum(listareal)-sum(lista)