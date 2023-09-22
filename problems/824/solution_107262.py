def uppCons(frase):
    tamanho = 0
    while tamanho < (len(frase))+1:
        frase.upper("a")
        frase.upper("e")
        frase.upper("i")
        frase.upper("o")
        frase.upper("u")
        tamanho = tamanho + 1
    return frase