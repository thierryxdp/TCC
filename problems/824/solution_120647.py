def uppCons(frase):
    ''' funcao que recebe uma frase e retorna a mesma frase so que com as consoantes em letra maiuscula. str -> str.'''
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    indice = 0
    while indice < len(consoantes):
        frase = frase.replace(consoantes[indice],consoantes[indice].upper()
        indice += 1
    return frase