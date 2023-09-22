def quant_palavras(frase):
    """Funcao que retorna o numero de palavras presentes na frase recebida de entrada
    string -> int"""
    frases_separadas = str.split(frase)
    return len(frases_separadas)