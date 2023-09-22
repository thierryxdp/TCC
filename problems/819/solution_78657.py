def filtraMultiplos(list, n):
    """..."""
    """list,int->list"""
    indice=0
    retorno=[]
    while indice < len(list):
        if list[0] % n == 0: