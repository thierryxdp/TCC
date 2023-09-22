def uppCons(frase):
    '''funçao que recebe uma frase de entrada e retorna todas
    as consoantes maiusculas e com os demais caracteres exatamente
    como estavam na frase original; str->str'''
    i=0
    nf=''
    c=bcdfghjklmnpqrstvwxyz
    while str.upper(frase):
        if frase[i]=c:
            i=i+1
        return nf