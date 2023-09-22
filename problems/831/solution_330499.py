def lingua_p(palavra):
    nova = ''
    vogal = 'a'
    for letra in palavra:
        if letra == vogal:
            vogal = list(vogal)
            nova = list(nova) + nova.append(vogal)
            nova1 = str(nova) + ''.join(nova)
        else:
            nova = list(nova) + nova.append(letra)
            nova1 = str(nova) + ''.join(nova)

    return nova1