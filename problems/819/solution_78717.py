def filtraMultiplos(list, n):
    """..."""
    """list,int->list"""
    indice=0
    resposta = list[]
    while indice < len(list):
        if list[indice] % n == 0:
            resposta = resposta + list[indice]
    
        indice = indice + 1
    return resposta