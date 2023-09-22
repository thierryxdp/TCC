def faltante(lista):
    '''funçãoq eu retorna o numero faltante da lista de peças
    de um quebra-cabeças
    list->int'''
    indice=0
    peca_faltante=0
    while indice<(len(lista)+1):
        peca_faltante=peca_faltante+(indice+1)
        indice=indice+1
    return peca_faltante-sum(lista)