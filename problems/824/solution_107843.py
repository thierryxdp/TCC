def uppCons(frase):
    '''função que retorna as consoantes em maiúsculo'''
    '''str-->str'''
    consoantes='bcdfghjklmnpqrstvwxyzç'
    x=''
    i=''
    contador=0
    while contador<len(frase):
        if frase[contador] in consoantes:
            i=str.upper(frase[contador])
            x=x+i
        else:
            x=x+frase[contador]
        contador=contador+1
    return x