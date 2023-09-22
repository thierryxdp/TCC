def faltante(lista):
    '''çlknhç'''
    quebra_cabecas=lista
    list.sort(quebra_cabecas)
    indice=0
    incide_posterior=1
    while indice<len(quebra_cabecas):
        if (quebra_cabecas[indice]+1)==quebra_cabecas[incide_posterior]:
            peca_faltante= quebra_cabecas[indice]+1
    indice=0
    incide_posterior=1
    return peca_faltante