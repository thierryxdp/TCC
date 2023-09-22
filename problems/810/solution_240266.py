def inverte(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',','')
    frase = frase.replace(':','')
    frase = frase.replace('.','')
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    
    frases = str.split(frase,' ')
    string_invertida = str.join(' ',frases[::-1])
    string_invertida = string_invertida.replace(' ','',1)
    return string_invertida.lower()