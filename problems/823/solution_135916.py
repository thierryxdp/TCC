def faltante(lista):
    i=0
    list.sort(lista)
    lista_maxima = list(range(min(lista),max(lista)+1))
    lst = []
    
    while i<len(lista):
        if lista[i] != lista_maxima[i]:
            list.append(lst,lista_maxima[i])
        i=i+1
    return lst[0]