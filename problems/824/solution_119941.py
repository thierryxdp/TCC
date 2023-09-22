def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com todas as consoantes em maiuscula
    str->str'''
    i=0
    Texto=''
    while i<len(frase):
        if frase[i] in 'bcdefghijklmnopqrstuvwxyz':
            Texto=Texto+str.upper(frase[i])
        else:
             Texto=Texto+frase[i]
            i=i+1
    return Texto