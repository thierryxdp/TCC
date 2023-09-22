def repetidos(x):
    ''' devolve a quantidade de reptições presentes na lista.
    lista -> int'''
    repeticoes = 0
    i = 0
    i2= i+1
    while i < len(x):
        if x[i] == x[i2]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes-1