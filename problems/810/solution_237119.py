def inverte(frase):
    '''função que dada uma frase, ela é invertida 
    sem pontuação e com letras minusculas
    entrada = str
    saida = str'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.lower(frase)
    frase = str.split(frase,' ')
    frase = frase[len(frase):0:-1]
    return str.join(str.split(frase,' '),frase)