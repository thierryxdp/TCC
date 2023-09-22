def quant_palavras(frase):
    """Função que recebe uma frase (frase) e retorna o 
    numero de palavras na frase;
    string -> int
    """
    f = frase.split()
    return len(f[0:])