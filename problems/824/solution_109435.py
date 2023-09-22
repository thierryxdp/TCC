uppCons (frase):
    '''Funcao que recebe uma frase e retorna a mesma com todas as consoantes em maiuscula'''
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra not in vogais:
            str.upper(letra)
    return frase