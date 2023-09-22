def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas suas consoantes maiúsculas: str -> str'''
    i = 0
    letra = frase[i]
    while i < len(frase):
        if not(letra in 'aeiouAEIOU'):
            str.replace(frase,str(letra),str.upper(letra)
        i += 1
    return frase