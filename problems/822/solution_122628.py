def repetidos(l):
    """
    retorna o numero de vezes que um numero é seguido de si mesmo na lista
    """
    i=1
    j=0
    while i<len(l):
        if l[i]==l[i-1]:
            j+=1
        i+=1
    return j