def repetidos(lista):
    i=0
    repeticao=0
    while i<(int(len(lista))-1):
        if lista[i]==lista[i+1]:
            repeticao=repeticao+1
    return repeticao