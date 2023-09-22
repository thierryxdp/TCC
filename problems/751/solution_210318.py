def quant_palavras(frase):
    """Função que dado uma frase, retorna o número de palavras dessa frase
    str -> int
    testes:
    quant_palavras("victor marinho") == 2
    quant_palavras("Turma de computação 1.") == 4
    """
    return len(str.split(frase))