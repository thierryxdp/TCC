def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    stringNova = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            att1 = stringNova + frase[contador]
            attt1.upper()
        else:
            att1 = stringNova + frase[contador]
        contador += 1
    return att1