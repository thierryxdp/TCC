def lingua_p(palavra):
    nova = ''
    vogal = 'a'
    for letra in palavra:
        if letra == vogal:
            vogal1 = list(vogal)
            nova = list(nova) + nova.append(vogal1)
            nova1 = str(nova) + ''.join(nova)
        else:
            nova = list(nova) + nova.append(letra)
            nova1 = str(nova) + ''.join(nova)

    return nova1