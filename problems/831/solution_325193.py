def lingua_p(palavra):
    '''Recebe uma string e retorna a palavra traduzida para a lingua do p;
Após cada vogal, é inserida a letra 'p' seguida da vogal original;
str => str'''
    n = list(str.lower(palavra))
    i = 0
    for x in n:
        if x in 'aeiou':
            x = str(x)+'p'+str(x)
            n[i] = x
        i = i+1
    return ''.join(map(str,n))