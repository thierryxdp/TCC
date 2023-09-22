def faltante(lista):
    '''çlknhç'''
    quebra_cabecas=lista
    list.sort(quebra_cabecas)
    indice=0
    indice_posterior=1
    peca_faltante=0
    while indice<len(quebra_cabecas):
        if (quebra_cabecas[indice]+1)!=quebra_cabecas[indice_posterior]:
            peca_faltante=peca_faltante+quebra_cabecas[indice]+1
    indice=indice+1
    indice_posterior=indice_posterior+1
    return peca_faltante