def lingua_p(palavra):
    palavra = palavra.lower()
    nova_Palavra = ''
    for letra in palavra:
        if letra in "aeiou":
            nova_Palavra += letra + "p" + letra
        else:
            nova_Palavra += letra
    return nova_Palavra