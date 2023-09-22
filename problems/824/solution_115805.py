def uppCons(frase):
    '''Função que dada uma frase, retorna a mesma com todas as consoantes
    em maiusculo
    str -> str'''
    indice = 0 
    frasenova = ''
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyzç':
            frasenova += str.upper(frase[indice])
        else:
            frasenova += frase[indice]
        indice += 1    
    return frasenova