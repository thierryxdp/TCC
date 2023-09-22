def uppCons(frase):
    i=0
    lista_str = []
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            list.append(lista_str,frase[i].upper())
        else:
            list.append(lista_str,frase[i])
        i=i+1
    return ''.join(lista_str)