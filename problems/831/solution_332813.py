def lingua_p(palavra):
    palavram = ' '
    vogal = 'aeiouAEIOU'
    for letra in palavra:
        if letra == vogal:
            palavra = letra + 'p'
    return palavram