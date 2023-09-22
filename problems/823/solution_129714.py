def faltante(lista_faltante):
    """coment"""
    lista_completa=list(range(1,len(lista_faltante)+2))
    i=0
    while lista_completa[i]==lista_faltante[i]:
        i+=1
        lista_completa.remove[lista_completa[i]]
    return lista_completa