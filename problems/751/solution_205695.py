def quant_palavras(frase):
    """Funçao que, ao receber uma frase, retorna o número de palavras da frase
       A frase pode possuir espaços no início e no final
       str->int"""
    frase=str.split(frase)
    return len(frase)