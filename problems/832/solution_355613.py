def eh_quadrada(matriz):
    '''recebe uma matriz e identifica se ela é quadrada
    list ->bool'''
    linham =len(matriz)
    colunam =len(matriz[0])
    quadrada =True
    if matriz ==[]:
        return quadrada
    if matriz[0] ==[]:
        return quadrada
   
    if linham ==colunam or linham==0 and colunam ==0:
        return quadrada
    else:
        return not quadrada