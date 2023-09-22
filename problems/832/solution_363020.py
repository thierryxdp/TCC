def eh_quadrada(matriz:list)->bool:
    """ identifica se uma matriz é quadrada ou nao"""
    linha=len(matriz)
    coluna=len(matriz[0])
    matriz=[]
    if linha!=coluna :
        mensagem=False
       
    else:
        mensagem=True
    return mensagem