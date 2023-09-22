def uppCons(s):
    '''Recebe uma frase e retorna a mesma frase porem com 
    todas as sua consoantes em maiusculas;
    str -> str'''
    cnt=0
    frase=''
    while cnt<len(s):
        if s[cnt] not in 'AEIOUaeiou':
            frase= frase + str.upper(s[cnt])
        if s[cnt] in 'AEIOUaeiou':
            frase = frase + s[cnt]
        cnt=cnt+1
    return frase