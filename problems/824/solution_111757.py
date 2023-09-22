def uppCons(frase):
    '''Função que rebece de entrada uma frase e retorna a mesma frase com todas as suas consoantes maiúsculas e demais caracteres em sua forma original'''
    '''str -> str'''
    letras = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzçñ':
            letras += str.upper(frase[i])
        else:
            letras += frase[i]
        i += 1
    return letras