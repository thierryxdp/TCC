from typing import str
from typing import int
def quant_palavras(frase: str) -> int
    """Essa função, dada uma frase como parâmetro de entrada,
    calcula e retorna o número de palavras da frase"""
    
    conta_palavras = len(str.split(frase))
    return conta_palavras