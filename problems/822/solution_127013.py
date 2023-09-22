def repetidos(lista):
    i=0
    list.sort(lista)
    repete=0
    while i< len(lista):
        if i== len(lista)-1:
            break
        if lista[i] == lista[i+1]:
            if list.count(lista,lista[i]) >2:
                i+= list.count(lista,lista[i])-2
                repete+= list.count(lista,lista[i])//2
        else:
            repete+=1
        i+=1
    return repete