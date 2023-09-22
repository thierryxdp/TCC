def eh_quadrada (x):
    ''' função que indentifica se uma certa matriz é quadrada '''
    ''' list[lista]->bool '''
    if len(m)==0:
        return (True)
    linha=len(matriz)
    coluna=len(matriz)
    if linha==coluna: 
        return (True)
    else:
        return (False)