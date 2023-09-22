def quant_palavras(frase):
    """Função que recebe uma frase e retorna o número de palavras desta frase;str->int"""
    return str.count(str.strip(str.split(frase)))