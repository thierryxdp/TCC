def inverte(frase):
    '''Dada uma frase retornará a frase em ordem inevrsa, sem letras maiusculas
    e pontuação.(str=>str>)'''

    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,':',' ')
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',frase)

    return frase