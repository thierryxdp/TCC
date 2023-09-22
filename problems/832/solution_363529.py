def eh_quadrada(matriz):
    """Função que dada uma matriz determina se ela é quadrada ou não"""
    """list-->bool"""
    if len(matriz)==len(matriz[0]):
        return True
    elif len(matriz[0])==0:
             return True
  	else:
        return False