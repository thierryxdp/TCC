def uppCons(frase):
    
    i=0
    vogais=list('AEIOUaeiou')
    lista = list(frase)
    
    while i < len(lista)-1:
        if lista[i] not in vogais:
            lista[i] = str.upper(lista[i])
        i += 1
    FRaSe = str.join(lista)
    return FRaSe