def lingua_p(palavra):
    palavra1 = palavra.lower()
    palavara2 = ''
    for p in palavra1:
        vogais = 'aãáeéiíoóuú'
        palavra2 += p
        if p in vogais:
            palavra2 += p + 'p'
    return palavra2