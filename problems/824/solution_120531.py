def uppCons (frase):
    i=0
    lista_frase = frase.split()
    consoante = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    while i < len(frase):
        if lista_frase in consoante: 
            lista_frase = lista_frase[i].upper()
        i = i+1
    return ''.join(lista_frase)