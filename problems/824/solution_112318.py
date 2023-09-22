def uppCons(frase):
    '''Recebe uma frase e retorna essa frase com as consoantes maiúsculas; str -> str'''
    i = 0
    resposta = ''
    while i < len(frase):
        a = frase[i]
        if a not in 'AEIOUaeiou ':
            a = str.upper(a)
        resposta = resposta + a
    return resposta