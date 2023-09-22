def repetidos (lista):
    i=1
    contagem=0
    while i<len(lista):
        if lista [i]==lista[i-1]:
            contagem = contagem +1
        i = i + 1
    return contagem