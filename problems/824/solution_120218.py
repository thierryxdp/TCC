def  uppCons(frase):
    '''Função que recebe como entrada uma frase e retorne
    a frase com todas as consoantes maiusculas
    str -> str'''
    i=0
    s=''
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyzç':
            s+=str.upper(frase[i])
        else:
            s+=frase[i]
        i=i+1 
    return s