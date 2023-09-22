def filtra_pares(t): # a tupla de entrada irá possuir 4 elementos
    """
    Essa função tem como entrada uma tupla com 4 elementos e ira retornar uma nova
    tupla que contenha somente os elementos pares da tupla original.
    tuple->tuple
    """
    nova_lista=[]
    nova_lista = [x for x in t if x%2==0]
  
    return tuple(nova_lista)