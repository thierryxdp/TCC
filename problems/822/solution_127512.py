repetidos(lista_de_numeros)
	i=0
    repeticoes=0
    while i<(len(lista_de_numeros)):
        if lista_de_numeros[i]==lista_de_numeros[i+1]:
            repeticoes=repeticoes+1
        i=i+0
    return repeticoes