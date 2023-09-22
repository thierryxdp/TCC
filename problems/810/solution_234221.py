def inverte(frase):
    """função que dada uma frase retorne outra frase com as mesmas palavras porém sem letras maiúsculas e sem pontuação.
    Exemplo: "Nossa, como eu gosto de chocolate" com a frase inversa -1 retorna "chocolate de gosto eu como nossa ". """

    lista = str.split(frase, "/")
    lista.reverse () 
    #lista list.reverse(frase)
    frase = str.join(" ",frase)

    return lista [-1]