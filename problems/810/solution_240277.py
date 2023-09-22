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
    return frase[-1:-(len(frase)+1):-1]