def uppCons(frase):
    '''recebe uma frase e retorna a frase com as consoantes maiúsculas;string->string'''
    i=0
    while len(frase)>i:
        if 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z' in frase[i]:
            up=str.upper(frase[i])
            reformed=frase.replace(frase[i], up)
            i+=1
        else:
            i+=1
    return reformed