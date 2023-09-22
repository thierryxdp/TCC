def uppCons(frase):
 	'''Recebe uma frase e retorna uma frase com apenas as consoantes em letras maiúsculas.
    str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou!.,ãúóáôí':
            str.upper(frase[i])
        i = i + 1
    return frase