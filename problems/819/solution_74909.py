def filtraMultiplos(listanum,n):
    '''diz se os numeeros da lista 'listanum' são multiplos de 'n''''
    i = 0
    a = []
    while i < len(listanum):
        if listanum[i]%n==0:
            a.append(listanum[i])
        i = i+1
    return a