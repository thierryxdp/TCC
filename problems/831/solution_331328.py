def lingua_p(palavra):
    v = "aáàâãeéèêêiíìîoóòôõuúùû"
    palavra = palavra.lower()
    nova_palavra = ""
    for letra in palavra:
        nova_palavra += letra
        if letra in v:
            nova_palavra += "p" + letra
    return nova_palavra