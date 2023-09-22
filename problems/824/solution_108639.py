def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    stringNova = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'aeiouAEIOU':
            stringNova = stringNova + frase[contador]
        else:
            stringNova = stringNova + frase[contador]
            stringNova.upper()
    return stringNova