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
    frase = str.lower(frase)
    frase = frase[-1:-(len(frase)+1):-1]
    return str.join(" ", frase)