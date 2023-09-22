def repetidos(lista):
    repticao=0
    for i in lista:
        if i==i-1:
            repeticao=repeticao+1
            i=i+1
    return repeticao