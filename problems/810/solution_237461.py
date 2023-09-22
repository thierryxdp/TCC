def inverte(frase):
    frase = frase.replace('-','').replace(',','').replace(':','').replace(';','').replace('.','').replace('!','').replace('?','')
    
    frase = str.split(frase,' ')
    frase = str.join(' ', frase[::-1])

    return frase