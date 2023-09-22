def inverte(frase):
    '''inverte recebe uma frase e devolve uma frase que contém as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem pontuação.
    str-->str.'''
    frase1=str.lower(frase)
    texto=str.replace(frase1,'!',' ')
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'...',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,';',' ')
    texto=str.split(texto)
    texto=texto[::-1]
    texto=str.join(' ',texto)

    return texto