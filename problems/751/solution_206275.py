# Calcula a quantidade de palavras de uma frase
# frase: string
# string -> int
def quant_palavras(frase):
    """Calcula a quantidade de palavras que a string 'frase' tem,
    considerando os espaços no início e no final"""
    return len(str.split(frase))