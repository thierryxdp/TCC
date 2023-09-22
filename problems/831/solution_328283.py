def lingua_p(palavra):
    palavra1 = palavra.lower()
    palavra2 = ''
    vogais = 'aãáeéiíoóuú'
    for p in palavra1:
        palavra2 += p
        if p in vogais:
            palavra2 += p + 'p'
    return palavra2