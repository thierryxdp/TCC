def quant_palavras(frase: str) -> int:
    """Dada uma frase, retorna o número de palavras da frase

       Parameters:
       frase: Uma string contendo uma frase

       Return:
       O número de palavras que a frase contém, dado o parâmetro "frase"

       Examples:
       quant_palavras("oi") == 1
       quant_palavras("oi oi") == 2
       quant_palavras("oi oi oi") == 3
    """
    
    x = str.split(frase)
    
    return len(x)