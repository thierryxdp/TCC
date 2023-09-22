def lingua_p(palavra):
    """retorna a frase de entrada com todas suas consoantes maiusculas """
    saida = []
    palavraP = []
    l = "p"
    for i in palavra:
        saida += i
        if i in "aeiou":
            strA = "".join('p')
            saida += strA
            saida += i
            palavraP = "".join(saida)
        else:
            palavraP += i
        
    return palavraP