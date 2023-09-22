def inverte(frase):
    frase=frase.replace('_','.').replace(',','.').replace('-','.').replace(':','.').replace(';','.').replace('!','.').replace('?','.').replace('...','.')
    frase=frase.split('.')    
    list.reverse(frase)
    frase=frase=str.join(' ',frase)
    return frase