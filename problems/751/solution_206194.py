def quant_palavras(frase):
    """Escreva uma frase entre "". A função retorna o número de palavras da frase.
    #parametros | in: Str (frase de entrada) -> out: int (num de palavras)"""
    return len(str.split(str.strip(frase)))