def inverte(frase):
    ''' funcao que recebe uma frase em string e retorna 
    frase= frase.lower()
    x= frase.replace('.',' ')
    x= x.replace('?',' ')
    x= x.replace(',',' ') 
    x= x.replace('-',' ')
    x= x.replace('!',' ')
    x= x.split()
    x.reverse()
    return str.join(' ',x)