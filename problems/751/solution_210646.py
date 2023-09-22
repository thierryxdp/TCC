def quant_palavras(frase):
    """Retorna o número de palavras de uma dada frase.
Assinatura: str -> list
Casos de teste:
("No news is good news") == 5
("SyntaxError: invalid syntax") == 3
"""
    return len(str.split(frase))