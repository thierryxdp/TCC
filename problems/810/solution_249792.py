def inverte(frase):
    '''dada uma frase, retorna a mesma, porém com as palavras em ordem inversa, sem letras maiúsculas e pontuações
       str -> str'''
    frase=frase.replace(',',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    frase.reverse()
    return str.join(' ',frase)