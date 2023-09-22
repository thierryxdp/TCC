def uppCons(frase):
    '''Esta e a funcao que recebe como 
    entrada uma frase e retorna a frase com todas 
    as consoantes em maiusculas'''
    s=''
    consoante='bcdfghjklmnpqrstvxwyz'
    j=0
    while j<len(frase):
        if frase[j] in consoante:
            s=s+frase[j].upper()
        j=j+1
    return s