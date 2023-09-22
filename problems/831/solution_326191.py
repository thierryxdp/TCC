def lingua_p(palavra):
    palavra = palavra.lower()
    vogal = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    lista = []
    for letra in palavra:
        if letra in vogal:
            list.append(lista, letra)
            list.append(lista, 'p')
            list.append(lista, letra)
        else:
            list.append(lista, letra)
    palavra = ''.join(lista)
    return palavra