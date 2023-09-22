def uppCons(frase):
    ''' função que recebe uma frase e retorna essa frase com todas as suas consoantes maiúsculas;
	str -> str '''
    x = 0
    frase = ''
    while x < len(frase):
        if (frase[x]) not in 'aàáãâeèéêiìíîoòóôõuùúû':
            frase = frase + frase[x].upper()
        else:
            frase = frase + frase[x].lower()
        x = x + 1
    return frase