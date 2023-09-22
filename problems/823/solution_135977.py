def faltante(lista):
    """Função que recebe uma lista com a sequência de peças de um quebra cabeça,
    e retorna o numero da peça faltante.
    list -> int"""
    
    i=0
    list.sort(lista)
    lista_maxima = list(range(1,max(lista)+1))
    lst = []
    if lista == lista_maxima:
        list.append(lst,max(lista)+1)
        
    while i<len(lista):
        if lista[i] != lista_maxima[i]:
            list.append(lst,lista_maxima[i])
        i=i+1
    return lst[0]