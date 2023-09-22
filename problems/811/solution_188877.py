def colchao(d, h, l):
    '''
    A função retorna True caso o colchão passe
    pela porte e False caso não passe
    (entrada = lista, int, int / saída = bool)
    '''
  if d[1] > h or d[2] > l:
        return False
    else:
        return True