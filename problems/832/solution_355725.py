def eh_quadrada (matriz):
    """Função que dada uma matriz retorna se ela é quadrada (True) ou não (False);
       list -> bool."""
    matriz_vazia = []
    if matriz == matriz_vazia:
        return True
    if len (matriz [0]) == len (matriz):
        return True
    else:
        return False