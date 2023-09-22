def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase, essa frase pode ter espaço no início e no final e as palavras são separadas por um único espaço
     string->int"""
    frase=str.split(frase)
    return len(frase)