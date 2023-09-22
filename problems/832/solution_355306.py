def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for;list->boolean'''
    nlinhas=len(matriz)
    i=0
    j=0
    while i<nlinhas:
        i+=1
    	ncolunas=len(matriz[0])
        while j<ncolunas:
            j+=1
    if i==j:
        return True
    else:
        return False