def uppCons(frase):
    '''função que recebe uma frase como entrada e retorna todas as consoartes da frase em maiúsculas. str -> str'''
    i = 0 
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in 'GKFCJFGFGHGFJgvgfdsesdkrhshrretru':
                 frase[i] = frase[i].upper()
    frase = ''.join(frase)
    return(frase)