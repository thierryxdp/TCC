def repetidos(lista):
    '''conta a quantidade de vezes que há repeticao entre dois numeros sucessivos de uma lista; list -> int'''
    i = 0
    contador = 0
    while i<len(lista)-1:
        if lista[i] == lista[i+1]:
            contador = contador + 1
        else:
            contador = contador
        i = i + 1
    return contador