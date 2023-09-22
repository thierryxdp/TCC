def faltante(lista):
    """ """
    i=0
    list.sort(lista)
    nova = list(range(1,len(lista)+2))
    t= len(lista)+1
    while i< t:
        if lista[i]!= nova[i]:
            return i
        i=i+1