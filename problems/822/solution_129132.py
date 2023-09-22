def repetidos(l):
    """Função que, ao receber uma lista de números, retorna o
    número de vezes que um elemento da lista se repete;
    list -> int."""
    newl = []
    for e in l:
        if l.count(e) > 1 and [e,e] in l:
            newl.append(e)
            l.remove(e)
    ret = len(newl)
    return ret