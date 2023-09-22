def inverte(frase):
    frase=frase.replace('_','.').replace(',','.').replace('-','.').replace(':','.').replace(';','.').replace('!','.').replace('?','.').replace('...','.')
    frase=frase.split('.')    
    frase=frase=str.join(' ',frase)
    list.reverse(frase)
    return frase