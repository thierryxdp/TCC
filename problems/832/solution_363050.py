def eh_quadrada(l):
    """Função que identifica se uma determinada matriz é quadrada.
    Obs: Uma matriz vazia (sem nenhuma linha e coluna) é quadrada>
    list -> bool
    """
    
    if (len(l) == len(l[0])):
        return True
    if (len(l[0])==0):
        return True
    else:
        return False