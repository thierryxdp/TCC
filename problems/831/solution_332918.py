def lingua_p(p):
    np = str.lower(p)
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in range(np):
        if np[i] in vogais:
            str.replace(np, np[i], np[i] + 'p' + np[i])
    return np