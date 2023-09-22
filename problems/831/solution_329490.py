def lingua_p(palavra):
    'dada uma palavra, ela é traduzida para a lingua do p str->str'
    n = len(palavra)
    m = 0
    while (n>m):
        if palavra[m] in str('AEIOUaeiou'):
            palavra = str.replace(palavra,palavra[m],palavra[m]+'p'+palavra[m])
            m = m+3
            n = len(palavra)
        else:
            m=m+1
    return palavra