def quant_palavras(frase: str) -> int:
    """Essa função, dada uma frase como parâmetro de entrada,
    calcula e retorna o número de palavras da frase"""
    
    #Separando todas as palavras da frase e as colocando em uma lista com a função split e as contando com a função len
    conta_palavras = len(str.split(frase))
    return conta_palavras