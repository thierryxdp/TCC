def lingua_p(palavra):
    'dada uma palavra, ela é traduzida para a lingua do p str->str'
    n = len(palavra)
    m = 0
    while (n>m):
        if palavra[m] in 'AEIOUáéíóúaeiou':
            palavrap = str.replace(palavra,palavra[m],palavra[m]+'p'+palavra[m])
            m = m+3
            n = len(palavrap)
        else:
            m=m+1
    return palavrap