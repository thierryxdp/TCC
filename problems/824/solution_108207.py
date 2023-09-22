def uppCons(frase):
    
    i=0
    consoantes_minusculas=list('bcçdfghjklmnpqrstvwxyz')
    consoantes_maiusculas=list(str.upper('bcçdfghjklmnpqrstvwxyz'))
    consoantes = consoantes_minusculas + consoantes_minusculas
    lista = list(frase)
    FRaSe = ''
    
    while i < len(lista):
        if lista[i] in consoantes:
            lista[i] = str.upper(lista[i])
        FRaSe += lista[i]
        i += 1
    
    return FRaSe