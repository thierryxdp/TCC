def faltante(lista):
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