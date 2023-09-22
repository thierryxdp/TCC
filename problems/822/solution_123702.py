def repetidos(lista):
    repeticoes=0
    i=0
    while i<len(lista):
        if lista[-len(lista)]==lista[len(lista)+1]:
            repeticoes+=1
        i+=1
    return repeticoes