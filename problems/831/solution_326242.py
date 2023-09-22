def lingua_p(palavra):
    palavra = palavra.lower()
    palavra = list(palavra)
    nova_Palavra = ''
    elemento = 0

    while elemento < len(palavra):
        letra = palavra[elemento]
        if letra in "aeiouáéíóúàèìòùâêîôûãõ":
            nova_Palavra += letra + "p" + letra
            elemento += 1
        else:
            nova_Palavra += letra
            elemento += 1

    return nova_Palavra