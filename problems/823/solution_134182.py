def faltante(lista):
    '''çlknhç'''
    quebra_cabecas=lista
    list.sort(quebra_cabecas)
    indice=len(quebra_cabecas)
    indice_posterior=indice-1
    peca_faltante=0
    while indice<0:
        if (quebra_cabecas[indice])!=quebra_cabecas[indice_posterior]:
            peca_faltante=peca_faltante+quebra_cabecas[indice]
    indice=indice-1
    indice_posterior=indice_posterior+1
    return peca_faltante