def uppCons(frase):
    '''
    função que recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas;
    str -> str
    '''
    i = 0
    frase = ''
    while i < len(frase):
        i = i + 1
        if frase[i] != 'AEIOUaeiou':
            frase = frase + str.upper(frase[i])
        else:
        return frase