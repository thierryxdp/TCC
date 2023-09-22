def uppCons(frase):
    '''retorna a frase com suas consoamtes maiusculas.str->str'''
    lista=list(frase)
    i=0
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyz':
            lista[i]=str.upper(lista[i])
        i=i+1
    return str.join('',lista)