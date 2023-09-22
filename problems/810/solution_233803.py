def inverte(frase):
    '''A partir de uma frase recebida, retorna outra frase com as mesmas palavras na ordem inversa;
    str => str'''
    return str.join(' ',str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.lower(frase),'.',''),'!',''),',',''),'?',''),'-',' '),' ')[-1::-1])