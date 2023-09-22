def inverte(frase):
    frase = str.replace(frase, "...", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, "/", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.split(frase)
    frase = frase[-1:-(len(frase)+1):-1]
    return join(" ", frase)