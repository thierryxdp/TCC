def lingua_p(palavra):
    palavram = ' '
    vogal = 'aeiouAEIOU'
    for letra in palavra:
        if letra == vogal:
            palavram = vogal + 'p'
    return palavra