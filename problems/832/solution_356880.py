def eh_quadrada(matriz):
    """retorna True se a matriz for quadrada e False se não for
    list(list)->bool"""
    if len(matriz)==len(matriz[0]):
        return True
    if len(matriz)==0:
        return True 
    else: 
        return False