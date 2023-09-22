def lingua_p(palavra):
    palavram = ' '
    vogal = 'aeiouAEIOU'
    for letra in palavra:
        if letra == vogal:
            palavram = letra + 'p'
    return palavram