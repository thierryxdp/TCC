def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    stringNova = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            stringNova = stringNova + frase[contador]
            stringNova = stringNova.upper()
        elif frase[contador] in 'aeiou':
            stringNova = frase[contador] + stringNova
        contador += 1
    return stringNova