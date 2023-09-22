def uppCons(string):
    "função que recebe uma frase e retorna essa frase com suas consoantes maiúsculas."
    j = 0
    x = ''
    while j < len(string):
        if string[j] in 'bcçdfghjklmnpqrstvwxyz':
            x = x + (string[j].upper())
        else:
            x = x + string[j]
        j = j + 1
    return x