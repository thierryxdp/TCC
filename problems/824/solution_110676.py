def uppCons(frase):
    ''' função que recebe uma frase e retorna essa frase com todas as suas consoantes maiúsculas;
	str -> str '''
    x = 0
    frase2 = ''
    while x < len(frase):
        if (frase[x]) not in 'aàáãâeèéêiìíîoòóôõuùúû':
            frase2 = frase2 + frase[x].upper()
        else:
            frase2 = frase2 + frase[x].lower()
        x = x + 1
    return frase2