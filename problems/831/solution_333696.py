def lingua_p(p):
    vogais = ['a','e','i','o','u']
    for f in range(len(p)):
        if p[f] in vogais:
            p = p[:f+1] + 'p' + p[f+1] + p[f+3:]
    return str.lower(p)