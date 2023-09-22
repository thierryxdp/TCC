def lingua_p(palavra):
    palavra = str.lower(palavra)
    palavra_nova = ""
    for indice in palavra:
        if indice in "AEIOUaeiou":
            palavra_nova = palavra_nova + indice + "p" + indice
        else:
            palavra_nova = palavra_nova + indice
    return palavra_nova