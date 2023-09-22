def uppCons(frase):
    
    i=0
    vogais=list('AEIOUaeiou')
    lista = list(frase)
    FRaSe = ''
    
    while i < len(lista):
        if lista[i] not in vogais:
            lista[i] = str.upper(lista[i])
        FRaSe += lista[i]
        i += 1
    
    return FRaSe