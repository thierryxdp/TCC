def faltante(L):
    """funcao que retorna o numero da peça faltando no quebra cabeça;list->int"""
    list.sort(L)
    i=0
    pecas=list(range(1,(1+L[(len(L)-1)])))
    while i<len(pecas):
        if pecas[i]!=L[i]:
            return pecas[i]
        else:
            return(len(L)+1)
        i=i+1