def eh_quadrada(matriz:list)->bool:
    """ identifica se uma matriz é quadrada ou nao"""
    linha=len(matriz)
    coluna=len(matriz[0])
    if matriz==[] or linha==coluna :
        mensagem=True
    else:
        mensagem=False
    return mensagem