def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    fraseNova = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            fraseNova += frase[indice]
            fraseNova2 = fraseNova.upper()
        indice = indice+1
        else:
            fraseNova2 += frase[indice]
    return fraseNova2