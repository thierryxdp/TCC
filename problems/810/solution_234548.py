def inverte(frase):
    '''função que dada uma frase retorna ela invertida sem caracteres especiais'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    frase = str.split(frase)
    frase = list.reverse(frase)
    novafrase = '' ''.join(frase)
    return novafrase