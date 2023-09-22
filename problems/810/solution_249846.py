def inverte(texto):
    ''' funçao que dada uma frase, retorna outra frase com as mesmas
    palavras na ordem inversa, sem letras maiusculas e sem a pontuaçao
    str->str
    '''
    e=str.replace(texto,'!','.')
    i=str.replace(e,'?','.')
    r=str.replace(i,'...','.')
    
    mini=str.lower(r)
    lista=str.split(mini)
    reverse= list.reverse(lista)
    return lista