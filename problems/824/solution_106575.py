def uppCons(frase):
    '''Dada uma frase, retorna a mesma, com todas as consoantes em maiúsculo'''
    '''str->str'''
    x=0
    cons=' '
    while x<len(frase):
        if frase[x] in 'AEIOUaeiou':
            cons=cons+frase[x]
        else:
            str.upper(frase[x])
            cons=cons+frase[x]
        x=x+1
    return cons