def lingua_p(palavra):
    contador=0
    for letra in palavra:
        if letra in "AEIOUaeiou":
            palavra[contador]='pe'