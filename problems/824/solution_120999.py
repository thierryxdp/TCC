def uppCons(frase):
    '''função que recebe uma frase e
    retorna a mesma com todas as suas consoantes maiusculas
    str --> str'''
    lista=list(frase)
    i=0
    while i<len(lista):
        x=str.upper(lista[i])
        if lista[i] in "bcdfghjklmnpqrstvwxyzç":
            del(lista[i])
            list.insert(lista,i,x)
        i=i+1
    return ''.join(lista)