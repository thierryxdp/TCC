def lingua_p(palavra):
    '''retorna a palavra dada subistituindo as vogais com ela, a letra p, e ela dnv'''
    retorna = palavra
    for i in palavra:
        if i in 'aeiouAEIOU':
            retorna=str.replace(retorna, i, (i +'p'+i))
    return retorna