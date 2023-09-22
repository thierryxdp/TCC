def lingua_p(p):
    i = 0
    vogais = ''
    while i < len(p):
        if p[i] in 'AEIOUaeiou':
            vogais = vogais + p[i] + 'p' + p[i]
        else:
            vogais = vogais + p[i]
        i = i + 1
    return vogais