def lingua_p(palavra):
    vogais = 'aeiouAEIOU'
    for i in palavra:
        if i in vogais:
            palavra = palavra[0:i] + 'p' + palavra[i:]
    return palavra