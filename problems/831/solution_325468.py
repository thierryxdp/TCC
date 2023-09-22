def lingua_p(palavra):
    """retorna a frase de entrada com todas suas consoantes maiusculas """
    saida = []
    for i in palavra:
        saida += i
        strA = "".join('p')
        strA = "".join(i)
        saida += strA
    return saida