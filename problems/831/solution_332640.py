def lingua_p(s):
    '''dada a variante, ele receba a palavra e retorna a mesma com "p" apos cada vogal da palavra original.str->str.'''
    vogal = ['a','e','i','o','u','á','é','ú',]
    lista =[]
    for i in range(0,len(s)):
        if (s[i] in vogal) == True:
            lista.append(s[i]+'p'+s[i])
        else:
            lista.append(s[i])
    return ''.join(lista)