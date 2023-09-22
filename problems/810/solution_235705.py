def inverte(frase):
    inv_frase = frase
    inv_frase = inv_frase.replace(',','')
    inv_frase = inv_frase.replace(':','')
    inv_frase = inv_frase.replace(';','')
    inv_frase = inv_frase.replace('-',' ')
    inv_frase = inv_frase.replace('!','')
    inv_frase = inv_frase.replace('?','')
    inv_frase = inv_frase.replace('.','')
    inv_frase = ' '.join(frase.split()[::-1])

    return inv_frase.lower()