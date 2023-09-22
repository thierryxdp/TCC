def inverte(frase):
    """str -> str;
    Função que, dada uma frase, retorna outra frase com as
    as mesmas palavras porém em ordem inversa, sem letras
    maiúsculas e sem pontuação."""
    s = '!?;,-.:'
    for x in s:
        frase = frase.replace( x , '')
    l = frase.split()
    ret = str.join(' ', l[-1::-1])
    return str.lower()