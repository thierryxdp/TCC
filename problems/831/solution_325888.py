def lingua_p(palavra):
    '''Retorna a palavra tradzida para a língua do P, ou seja, após cada vogal
       sera adicionado 'p' mais a vogal.
       str -> str'''
    i = 0
    palavra = str.lower(palavra)
    while i <= (len(palavra)-1):
        if palavra[i] in 'aeiou':
            palavra = palavra[:i+1] + 'p' + palavra[i] + palavra[i+1:]
            i = i + 3
        else:
            i = i + 1
    return palavra