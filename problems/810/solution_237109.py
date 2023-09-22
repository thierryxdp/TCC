def inverte(frase):
    '''função que dada uma frase, ela é invertida 
    sem pontuação e com letras minusculas
    entrada = str,list
    saida = str'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.lower(frase)
    frase = str.split(frase,' ')
    frase = str.join(' ',frase)
    frase = frase[frase:0:-1]
    return frase