def repetidos(numeros):
    i=1
    qtd=0
    while i<len(numeros):
        if numeros[i] in '1234567890':
            qtd = numeros[i]==numeros[i-1]
            qtd = qtd+1
    return qtd