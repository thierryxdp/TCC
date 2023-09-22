def repetidos(lista_de_numeros):
    repeticoes=0
    i=0
    while i<len(lista_de_numeros):
        if lista_de_numeros[i-1]==lista_de_numeros[i]:
            repeticoes=repeticoes+1
            i=i+1
        else:
            i=i+1
    return repeticoes

repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7])