def uppCons(frase):
    '''função que dada uma frase, retorna a mesma com todas
    as suas consoantes em maiúsculas  ent-> str   saida-> str'''
    frase2 = frase.split()
    indice = 0
    
    while indice < len(frase2):
        if frase2[indice] not in 'bcdfghjklmnpqrstvwxyz':
            letra = frase2[indice]
            newletra = str.upper(letra)
            del frase2[indice]
            list.insert(frase2, indice, newletra)
            indice = indice + 1
    frase3 = ''.join(frase2)
    return frase3