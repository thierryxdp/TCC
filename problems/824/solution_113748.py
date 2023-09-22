def uppCons(frase):
    '''
    função que recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas;
    str -> str
    '''
    i = 0
    frase = ''
    while i < len(frase):
        if frase[i] != 'AEIOUaeiou':
            frase = frase + str.upper(frase[i])
        i = i +1
        return frase