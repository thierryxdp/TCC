def lingua_p(palavra):
    palavram = ' '
    vogal = 'aeiouAEIOU'
    for letra in palavra:
        if letra == vogal:
            palavra = palavram + 'p'
    return palavram