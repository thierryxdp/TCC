def faltante(lista):
    """Essa função retorna a peça faltante. Como entrada temos 
    uma lista, e como saída temos o número da peça faltante;
    list->int"""
    indice=0
    contagem=0
    list.sort(lista)
    while indice<len(lista):
        if indice+1==lista[indice]:
            contagem=contagem+1
        indice+=1
    return contagem+1