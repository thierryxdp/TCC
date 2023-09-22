def uppCons(frase):
    '''funcao que retorna a frase com todas as consoantes maiusculas
    str->str'''
    texto=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyzç':
            texto+=frase[i]
        i=i+1
    return texto