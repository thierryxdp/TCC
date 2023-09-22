def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiusculas
    string -> string'''
    i=0
    frase2=[]
    while i<len(frase):
        if str.lower(frase[i]) in 'bcdfghjklmnpqrstvxywzç':
            list.append(frase2,str.upper(frase[i]))
        else:
            list.append(frase2,frase[i])
        i=i+1
    str.join('',frase2)
    return frase2