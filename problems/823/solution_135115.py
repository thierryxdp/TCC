def faltante(L):
    """Função que recebe N números inteiros de 1 a N, com um deles faltando.
    A função retorna exatamente qual é o número faltante.
    list->int"""
    list.sort(L)
    indice=0
    if 1 not in L:
        return 1
    while indice<(len(L)-1):
        if ((L[indice+1])-1)!=L[indice]:
            return indice+2
        indice=indice+1
    return "Não há nenhum número faltando"