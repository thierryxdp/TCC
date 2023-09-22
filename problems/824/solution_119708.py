def uppCons(frase):
    '''função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculas'''
    consoante = 'bcçdfghjklmnpqrstvwxz'
    proximo = 0
    nova_frase = ''
    while proximo < len(frase):
        if frase[proximo] in consoante:
           nova_frase = nova_frase+frase[proximo].upper()
        else:
            nova_frase = nova_frase+frase[proximo]
        proximo = proximo +1
    return nova_frase