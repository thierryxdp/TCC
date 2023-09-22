def quant_palavras(frase):
    """Função recebe uma frase e retorna a quantidade de 
    palavras da frase;
    str -> int"""
    palavras = str.split(frase)
    return len(palavras)