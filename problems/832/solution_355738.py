def eh_quadrada(matriz:list)->bool:
    """Dada uma matriz, retorna se ela é quadrada, dizendo True se ela é, ou False em caso contrário."""
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False