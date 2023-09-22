def faltante(listaPecas):
    """identifica e retorna o valor numerico da peça faltante da lista;
    list->int"""
    
    lista=[]
    i = 0
    
    listaPecas.sort()
    
if len(listaPeças) - 1 > 1:
    while i < (len(listaPecas)-1):
        if listaPecas[i+1] - listaPecas[i] > 1:
            return i + 2
        i+=1
    if listaPecas[0] == 1:
        return listaPecas[-1] + 1
    else:
        return listaPecas[0]-1