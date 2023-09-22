def faltante(listaPeças):
    """identifica e retorna o valor numerico da peça faltante da lista;
    list->int"""
    lista=[]
    i = 0
    listaPeças.sort()
    while i < (len(listaPeças)-1):
        if listaPeças[i+1] - listaPeças[i] > 1:
            return i + 2
    if listaPeças[0] == 1:
        return listaPeças[-1] + 1
    else:
        return listaPeças[0]-1