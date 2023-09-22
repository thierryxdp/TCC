def quant_palavras(frase):
    """Função que recebe uma string e retorna o número de palavras da frase desconsiderando os espaços. str -> int"""
    frase = frase.split()
    return len(frase)