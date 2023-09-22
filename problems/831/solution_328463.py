def lingua_p(palavra):
    saida = ''
    palavra = str.lower(palavra)
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáàâãéêíóôõ':
            saida = saida + palavra[i] + 'p' + palavra[i]
       	else:
            saida = saida + palavra[i]
    return saida