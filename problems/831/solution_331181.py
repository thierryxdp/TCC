def p(palavra):
    vogais = 'aeiouáéíóúãõ'
    palavram = palavra.lower()
    np = '' 
    for p in palavram:
        np += p
        if p in vogais:
            np += 'p' + p
    return np