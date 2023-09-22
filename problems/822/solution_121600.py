def repetidos(lista):
    i =0
    count =0
    while i+1 <len(lista):
        if lista[i+1] ==lista[i]:
            count =count +1
        i =i+1
    return count