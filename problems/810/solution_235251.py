def inverte(frase):
    '''Função que dada uma frase, retorne outra frase que contenha as mesmas plavras da frase de entrada na ordem inversa 
    str ->str'''
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.split(frase)[-1::-1]
    frase= str.join(' ',frase)
    return str.lower(frase)