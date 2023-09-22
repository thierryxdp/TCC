def inverte(frase):
    inv_frase = ' '.joint(frase.split()[::-1])
    inv_frase = inv_frase.replace(',',' ')
    inv_frase = inv_frase.replace(':',' ')
    inv_frase = inv_frase.replace(';',' ')
    inv_frase = inv_frase.replace('-',' ')
    inv_frase = inv_frase.replace('!',' ')
    inv_frase = inv_frase.replace('?',' ')
    return inv_frase.lower()