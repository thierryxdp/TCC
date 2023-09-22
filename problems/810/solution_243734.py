def inverte(phrase):
    """funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
frase = str.split(frase, "-")
frase = str.join(" ", frase)
frase = str.split(frase, ",")
frase = str.join(" ", frase)
frase = str.split(frase, ":")
frase = str.join(" ", frase)
frase = str.split(frase, ";")
frase = str.join(" ", frase)
frase = str.split(frase, ".")
frase = str.join(" ", frase)
frase = str.split(frase, "?")
frase = str.join(" ", frase)
frase = str.split(frase, "!")
frase = str.join(" ", frase)
lista.reverse(frase)
frase = str.join(" ", lista)
                 return frase