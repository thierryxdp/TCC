def uppCons (frase):
    i=0
    lista_frase = frase.strip()
    consoante = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    while i < len(frase):
        if consoante in lista_frase: 
            lista_frase = lista_frase.upper()
        i = i+1
    return ''.join(lista_frase)