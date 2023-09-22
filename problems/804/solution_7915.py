def filtra_pares(tup):
    """ Dado uma tupla com 4 elementos,vamos retornar somentos os elemtos pares na mesma ordem que nos foi passado.
        Parametros:
        Entrada -> tupla
        Saida   -> tupla   """
    w=()
    if tup[0]%2==0:
        w=w+(tup[0],)
    if tup[1]%2==0:
        w=w+(tup[1],)
    if tup[2]%2==0:
        w=w+(tup[2],)
    if tup[3]%2==0:
        w=w+(tup[3],)
        return w
    else:
        return w