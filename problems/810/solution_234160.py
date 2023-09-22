def inverte(frase):
    '''a função que dada uma frase retorne uma outra frase que contenha as mesmas
    palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a
    pontuação.
    str->str '''
    z=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace
    (str.replace(frase,'!',''),'...',''),'?',''),'-',''),':',''),';',''),',',''),'.','')
    y=str.lower(z)
    p=str.split(y)
    x=p[::-1]
    x1=' '.join(x)
    return x1