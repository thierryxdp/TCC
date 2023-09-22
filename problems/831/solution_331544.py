def lingua_p(string):
    ''' uma funcao que recebe uma palavra em portugues e retorna essa mesma
    palavra traduzida para a lingua do P.
    str -> str'''
    resposta = ''
    letra = ''
    palavra = str.lower(string)
    for i in palavra:
        if i in 'aeiouáéí':
            letra = i + 'p'
            resposta += letra
        resposta += i
    return resposta