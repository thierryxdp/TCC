def lingua_p():
    l=palavra
    contador=0
    while contador <len(palavra):
        if palavra[contador] in 'AEIOUaeiou':
            l=l[0:contador] + 'p' + l[0:]
        contador=contador+1
    return str.lower(l)