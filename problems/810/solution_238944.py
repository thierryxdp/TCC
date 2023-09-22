def inverte(frase):
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    frase = frase.replace(',','')
    frase = frase.replace('.','')
    frase = frase.replace('-',' ')
    invertida = (str.split(frase,' '))
    lista = (str.join(' ',invertida[::-1]))
    return lista.lower