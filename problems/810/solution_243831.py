def inverte(frase):
    """funcao que dada uma frase retorna uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa 
        com todas as pontuacao sendo trocadas por espaco em branco
        str -> str"""
    frase = str.lower(frase)
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
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase