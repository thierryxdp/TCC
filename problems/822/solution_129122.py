def repetidos(l):
    """Função que, ao receber uma lista de números, retorna o
    número de vezes que um elemento da lista se repete;
    list -> int."""
    newl = []
    for i in l:
        if l[i] == l[(i+1)]:
            newl.append(e)
            l.remove(e)
        #if l.count(e) > 1:
         #   newl.append(e)
          #  l.remove(e)
    ret = len(newl)
    return ret