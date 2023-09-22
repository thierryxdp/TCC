def uppCons(frase):
    '''recebe uma frase retorna a mesma frase com as consoante em caixa alta'''
    y= lambda x: x.upper() if x not in 'aeiou' else x
    s=list(map(y,frase))
    s=''.join(s)
    return s