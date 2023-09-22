def repetidos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] == lista[i+1]:
            soma=soma+1
        i=i+1
    return soma