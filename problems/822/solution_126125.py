def repetidos(lista):
    i = 1
    iguais = 0 
    while i < len(lisa):
        if lista[i] == lista[i-1]:
            iguais = iguais + 1 
        i = i + 1
    return iguais