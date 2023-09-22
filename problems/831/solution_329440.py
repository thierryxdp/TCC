def lingua_p(palavra):
    l=palavra
    contador=0
    while contador <len(palavra):
        if palavra[contador] in 'AEIOUaeiou':
            l=l[0:contador+1] + 'p' + l[:0]
        contador= contador +1
    return str.lower(l)