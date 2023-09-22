def uppCons(frase):
    '''recebe como entrada uma frase e retorna a mesma frase com as consoantes maiúsculas; str->str'''
    i=0
    while i<len(frase):
        if 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z' in frase[i]:
            m=str.upper(frase[i])
            n=frase.replace(frase[i],m)
            i+=1
        else:
            i+=1
    return n