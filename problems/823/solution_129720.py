def faltante(lista_faltante):
    """coment"""
    lista_completa=list(range(1,len(lista_faltante)+2))
    i=0
    j=0
    lista_faltante.sort()
    while i,j<len(lista_faltante):
        i+=1
        j+=1
        if lista_completa[i]!=lista_faltante[i]:
            return lista_completa.pop(i)