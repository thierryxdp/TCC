def quant_palavras(frase):
    """Funcao retorna quantas palavras existem em uma frase dada
    na forma de string: frase """

    retira_pontuacao(frase)
    
    p = frase.split(" ")

    p = list(filter(lambda x: x != "", p))
    
    return len(p)