def uppCons(frase):
    '''descricao'''
    i=0
    while i<=len(frase):
        if i not in 'aeiou':
            i=i+1
    return str.join(str.upper(frase[i]))