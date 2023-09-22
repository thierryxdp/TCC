def lingua_p(palavra):
    palavra=str.lower(palavra)
    linguaP=str()
    for letra in palavra:
        if letra in "aeiou":
            linguaP=linguaP+letra+"p"+letra
    return LinguaP