def eh_quadrada(matriz):
    """ Dado uma matriz vamos verificar se ela é quadrada (True) ou não (False).
        Parametros:
        Entrada -> matriz : list
        Saida   -> bool  """
    m=matriz
    num_linha=len(m)
    num_coluna=len(m[0])
    if num_linha==num_coluna:
        return True
    return False