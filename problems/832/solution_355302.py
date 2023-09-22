def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    i=0
    j=0
    while i<ncolunas:
        i+=1
        while j<nlinhas:
            j+=1
    if i==j:
        return True
    else:
        return False