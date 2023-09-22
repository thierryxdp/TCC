def inverte(frase):
    """
    Função que dada uma frase retorne outra que contenha as mesmas palavras da frase inserida, na ordem inversa, sem letras maiúsculas e pontuação
    str-> str
    
    Parameters:
    frase: Parâmetro do tipo str que representa a frase inserida
    """
    nfrase = str.lower(frase[:])
    for caractere in ["-", ",", ":", ";" , ".", "!", "?", "..."]:
        nfrase = str.replace(nfrase, caractere, " ")

    lista = str.split(nfrase)
    lista.reverse()

    nfrase = str.join(" ", lista)

    return nfrase