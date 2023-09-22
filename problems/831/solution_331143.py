def lingua_p(palavra):
    texto=""
    for letra in palavra:
        if letra in "AEIOUaeiou":
            texto=texto+letra+p+letra
    return texto