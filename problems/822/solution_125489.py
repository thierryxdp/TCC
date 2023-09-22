def repetidos(lista):
    '''dada uma lista de numeros, a funçao devolve o numero
    de vezaes que um numero é igual ao numero anterior;
    list-->int'''
    i=1
    repeticoes=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes