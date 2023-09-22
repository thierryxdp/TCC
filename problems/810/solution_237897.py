def inverte(x: str) -> str:
    """Dada uma frase, retorna essa mesma frase com as palavras na ordem
       inversa, sem letras maiúsculas e sem pontuação

       Parameters:
       x: Frase a ser modificada

       Return:
       Dado o parâmetro "x", retorna a mesma string do parâmetro com as
       palavras na ordem inversa, sem letras maiúsculas e sem pontuação

       Examples:
       inverte("Nossa, como eu gosto de chocolate.") ==
       'chocolate de gosto eu como nossa'
       inverte("Ola, Pyhton") == 'pyhton ola'
       inverte("Feliz aniversário") == 'aniversário feliz'
    """
    a = str.replace(x, "-", " ")
    b = str.replace(a, ",", " ")
    c = str.replace(b, ":", " ")
    d = str.replace(c, ";", " ")
    e = str.replace(d, ".", " ")
    f = str.replace(e, "!", " ")
    g = str.replace(f, "?", " ")

    y = str.lower(g)

    z = str.split(y)
    w = list.reverse(z)
    k = str.join(" ", z)

    return k