def uppCons(frase):
    '''retorna a frase de entrada com todas as consoantes em maiusculo
    str-->str'''
    i=0
    lista=list(frase)
    while(i<len(lista)):
        if(lista[i] in 'bcdfghjklmnpqrstvwxyzç'):
            lista[i]=str.upper(lista[i])
        i+=1
    novafrase=str.join('',lista)
    return novafrase