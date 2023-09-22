def repetidos(lista_de_numeros):
	i=0
    repeticoes=0
    while i<(len(lista_de_numeros)):
        if lista_de_numeros[i+1]==lista_de_numeros[i]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes