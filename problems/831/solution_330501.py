def lingua_p(palavra):
    nova = ''
    vogal = 'a'
    for letra in palavra:
        if letra == vogal:
            nova = nova + vogal
            nova1 = nova + ''.join(nova)
        else:
            nova = nova + letra
            nova1 = nova + ''.join(nova)

    return nova1