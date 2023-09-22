def uppCons(frase):
    '''função que recebe uma frase como entrada e retorna todas as consoartes da frase em maiúsculas. str -> str'''
    i = 0 
    while i < len(frase):
        if frase[i] is not 'aeiouAEIOUãáàéèíóôú':
            frase = frase.replace(frase[i],frase[i].upper())
        i=  i + 1
    return(frase)