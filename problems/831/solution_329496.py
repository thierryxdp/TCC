def lingua_p(palavra):
    'dada uma palavra, ela é traduzida para a lingua do p str->str'
    n = len(palavra)
    m = 0
    palavra == palavrap
    while (n>m):
        if palavra[m] in str('AEIOUáéíóúaeiou'):
            palavrap = str.replace(palavrap,palavra[m],palavra[m]+'p'+palavra[m])
            m = m+1
        else:
            m=m+1
    return palavrap