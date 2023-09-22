def inverte(frase):
    inv_frase = frase
    inv_frase = inv_frase.replace(',','')
    inv_frase = inv_frase.replace(':','')
    inv_frase = inv_frase.replace(';','')
    inv_frase = inv_frase.replace('-',' ')
    inv_frase = inv_frase.replace('!','')
    inv_frase = inv_frase.replace('?','')
    inv_frase = inv_frase.replace('.','')
    inv_frase = ' '.join(inv_frase.split()[::-1])

    return inv_frase.lower()