def eh_quadrada(matriz:list)->bool:
    for i in matriz:
        if len(matriz)!=len(i):
            return False
    return True