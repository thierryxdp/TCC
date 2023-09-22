def repetidos(l):
    """Função que, ao receber uma lista de números, retorna o
    número de vezes que um elemento da lista se repete;
    list -> int."""
    newl = []
    prox = 0
    while prox < len(l):
        if l[prox] == l[prox - 1]:
            newl.append(prox)
        prox = prox + 1
    #for e in l:
    #    if l.count(e) > 1:
     #       newl.append(e)
      #      l.remove(e)
    ret = len(newl)
    return ret