def faltante(lista_faltante):
    """coment"""
    lista_completa=list(range(1,len(lista_faltante)+2))
    i=0
    lista_faltante.sort()
    lista_faltante.append("")
    while i<len(lista_completa):
        i+=1
        if lista_faltante[0]==2:
            return 1
        if lista_completa[i]!=lista_faltante[i]:
            return lista_completa.pop(i)