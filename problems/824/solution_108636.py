def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    stringNova = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            stringNova = stringNova + frase[contador]
            stringNova = stringNova.upper()
       	else:
            return 0
        contador += 1
    return stringNova