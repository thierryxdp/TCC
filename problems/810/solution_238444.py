def inverte (frase):
    '''Função que dada uma frase, retorna uma outra frase com as mesmas
    palavras invertidas,sem pontuação e sem letras maiusculas'''
    frase= str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace (frase,'.',' '),'!',' '),'?',' '),'-',' '),';',' '),',',' '),':',' '))
    frasei= str.split(frase)[::-1]
    return str.join (' ',frasei)