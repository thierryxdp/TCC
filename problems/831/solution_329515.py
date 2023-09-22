def lingua_p(palavra):
    'dada uma palavra, ela é traduzida para a lingua do p str->str'
    n = len(palavra)
    m = 0
    k = palavra[m]
    while (n>m):
        if palavra[m] in str('AEIOUáéíóúaeiou'):
            palavra = str.replace(palavra,k,k+'p'+k)
            n = len(palavra)
            m = m+3
        else:
            m=m+1
    return palavra