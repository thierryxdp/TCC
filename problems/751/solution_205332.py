def quant_palavras(frase):
    """
    Calcula o número de palavras em uma frase.
    str -> int.

    Parameters:
    frase: Parâmetro textual, do tipo string (str);
    
    Returns:
    A quantidade de palavras em uma frase.
    """  
    x = frase.split()
    return len(x)