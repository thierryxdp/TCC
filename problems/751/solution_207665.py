def quant_palavras(x):
    """dada uma frase string como entrada, retorna o numero de palavras que ela possui;
    str->int"""
    teste=x
    teste1=teste.split()
    return len(teste1)