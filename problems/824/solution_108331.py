def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    fraseNova = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            fraseNova = frase.replace(frase[indice],'teste')
        indice = indice+1
    return fraseNova