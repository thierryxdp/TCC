def quant_palavras(frase):
    """Função que, dada uma frase, retorna o número de palavras da frase
    Entrada: String
    Saída: Int"""
    
    return len(str.split(str.strip(frase)))