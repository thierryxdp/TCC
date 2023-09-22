def lingua_p(palavra):
    palavra=str.lower(palavra)
    linguaP=str()
    for letra in palavra:
        if letra in "aeiouáéíóú":
            linguaP=linguaP+letra+"p"+letra
        else:
            linguaP=linguaP+letra
    return linguaP