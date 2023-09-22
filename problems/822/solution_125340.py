def repetidos(lista):
    i = 0
    cnt=0
    while i < len(lista):
        elem= lista[i]
           if elem != lista[i]:
                   cnt=+1
            i+=1
    return cnt