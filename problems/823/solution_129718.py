def faltante(lista_faltante):
    """coment"""
    lista_completa=list(range(1,len(lista_faltante))
    i=0
    lista_faltante.sort()
    while i<len(lista_completa):
        i+=1
        if lista_completa[i]!=lista_faltante[i]:
            return lista_completa.pop(i)