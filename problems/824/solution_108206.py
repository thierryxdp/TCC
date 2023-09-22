def uppCons(frase):
    
    i=0
    consoantes_minusculas=list('bcdfghjklmnpqrstvwxyz')
    consoantes_maiusculas=list(str.upper('bcdfghjklmnpqrstvwxyz'))
    consoantes = consoantes_minusculas + consoantes_minusculas
    lista = list(frase)
    FRaSe = ''
    
    while i < len(lista):
        if lista[i] in consoantes:
            lista[i] = str.upper(lista[i])
        FRaSe += lista[i]
        i += 1
    
    return FRaSe