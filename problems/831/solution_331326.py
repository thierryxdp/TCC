def lingua_p(palavra):
    v = "aeiou"
    palavra = palavra.lower()
    nova_palavra = ""
    for letra in palavra:
        nova_palavra += letra
        if letra in v:
            nova_palavra += "p" + letra
    print(nova_palavra)