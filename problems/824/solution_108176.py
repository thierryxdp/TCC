def uppCons(frase):
    i=0
    vogais=list('AEIOUaeiou')
    lista_frase = list(frase)
    FRaSe = ''
    while i < len(lista_frase) - 1:
        if list(frase)[i] not in vogais:
            list(frase)[i] = str.upper(list(frase)[i])
        i += 1
        FRaSe += list(frase)[i]
    return FRaSe