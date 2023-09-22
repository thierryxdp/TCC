# retorna a frase entrada na ordem inversa, sem letras maiúsculas e sem pontuação
def inverte(texto):
    texto = texto.lower()
    texto = texto.replace("-", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    texto = texto.replace("...", " ")
    texto = texto.split()
    texto.reverse()
    texto = tuple(texto)
    texto = str.join(" ",texto)
    return texto