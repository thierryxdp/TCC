def inverte(frase):
    '''função que dado uma string, retorna outra string com as mesmas palavras
    na ordem, inversa, com  todas as letras minuscúlas e sem pontuação
    str -> str'''
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('^',' ')
    frase = frase.replace('~',' ')
    frase = frase.replace('´',' ')
    frase = frase.replace('`',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('/',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('_',' ')
    frase = str.split(frase) [-1::-1]
    frase = str.join(' ',frase)
    return str.lower(frase)