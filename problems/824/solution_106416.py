def uppCons(frase):
    '''recebe como entrada uma frase e retorna a mesma frase com as consoantes maiúsculas; str->str'''
    i=0
    while i<len(frase):
        if not 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U' in frase[i]:
            m=str.upper(frase[i])
            n=frase.replace(frase[i],m)
            i+=1
        else:
            i+=1
    return p