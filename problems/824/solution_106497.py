def uppCons(frase):
    '''uppCons recebe uma lista e devolve outra lista
    Coloca todas as consoantes da lista em maiusculo
    list --> list'''
    novafrase=''
    contadora=0
    while contadora<len(frase):
        letras=frase[contadora]
        if letras in 'bcçdfghjklmnpqrstvwxyz':
            letras=str.upper(letras)
        contadora=contadora+1
        novafrase=novafrase+letras
    return novafrase