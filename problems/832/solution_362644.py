def eh_quadrada (matrix=[]):
    ''' list[lista]->bool '''
    if len(matriz)==0:
        return(True)
    linha=len(matriz)
    coluna=len(matriz[0])
    if linha==coluna: 
        return (True)
    else:
        return(False)