# recebe uma frase e retorna quantas palavras estão dentro dessa frase
# string -> int
def quant_palavras(frase):
    """recebe uma frase inteira e retorna a quantidade de palavras individuais dentro dela, string->int """
    return len(str.split(frase))