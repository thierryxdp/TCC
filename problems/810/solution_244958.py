def inverte(frase):
    '''
       bla
    '''
    
    frase = frase.replace(',','')
    frase = frase.replace('-','')
    frase = frase.replace(':','')
    frase = frase.replace(';','')
    frase = frase.replace('.','')
    frase = frase.replace('?','')
    frase = frase.replace('!','')
    splitar = frase.split(',')
    splitar = splitar[::-1]
    
    return ((','.join(splitar)).replace(',',''))