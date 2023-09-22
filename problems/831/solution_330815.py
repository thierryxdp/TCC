def lingua_p(p):
    i = 0
    vogais = ''
    while i < len(p):
        if p[i] in 'AEIOUaeiou':
            vogais = vogais + 'i'
        i = i + 1
    return vogais