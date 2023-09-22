def lingua_p(palavra):
    ''' Função que coloca uma letra p antes da vogal.
    str -> str'''
    lower = palavra.lower()
    new = ''
    vogais = 'aeiouãáéíóú'
    for p in lower:
        new += p
        if p in vogais:
            new += 'p' + p

    return new