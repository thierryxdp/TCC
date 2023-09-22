def uppCons (frase):
    i=0
    lista_frase = frase.strip()
    consoante = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    while i < len(frase):
        if lista_frase[i] in consoante:
            lista_frase[i] = lista_frase[i].upper()
        i = i+1
    return ''.join(lista_frase)