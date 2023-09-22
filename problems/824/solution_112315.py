def uppCons(frase):
    '''Recebe uma frase e retorna essa frase com as consoantes maiúsculas; str -> str'''
    i = 0
    resposta = ''
    while i < len(frase):
        a = lista[i]
        if a not in 'AEIOUaeiou ':
            b = str.upper(a)
        resposta = resposta + b
    return resposta