def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiusculo
    str -> str'''
    i=0
    novafrase = ''
    while i < len(frase):
        consoante = frase[i]
        maiusculo = consoante.upper()
        novafrase = novafrase + maiusculo
        i = i + 1
        return novafrase