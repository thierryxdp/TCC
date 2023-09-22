def uppCons(frase):
    '''funçao que dada uma frase retorna todas as consoantes presentes nela 
    em maiusculo'''
    fraseNova = ''
    indice = 0
    while indice < len(frase):
        fraseNova + frase.replace(frase[indice],str.upper(frase[indice])