def inverte(frase):
    """funcao que dada uma frase retorna uma outra frase que contenhas
    as mesmas palavras da frase de entrada na ordem invertida sem letras
    maiusculas e sem pontuacao.
    Exemplo: "Nossa, como eu gosto de chocolate" com a frase invertida
    sem pontuacao e sem letras maiusculas a frase retorna "Chocolate
    de gosto como nossa". """
    lista = str.split(frase)
    lista.inverse()
    #lista = list.reverse(frase)
    frase = str.join(" ",frase)
    return frase