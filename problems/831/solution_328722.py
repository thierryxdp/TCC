def lingua_p(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'é', 'ê', 'í', 'ó', 'õ', 'ô', 'ú']
    i = 0
    palavraP = []
    for letra in palavra:
        if letra in vogais:
            list.append(palavraP, letra)
            list.append(palavraP, 'p')
            list.append(palavraP, letra)
        else:
            list.append(palavraP, letra)
    return str.lower(str.join(",palavraP))