def quant_palavras(frase):
    """Essa função retorna o número de palavras dada uma frase.Como
    entrada temos a frase(string) e como saída temos a quantidade 
    de palavras nessa frase(inteiro);
    string -> int"""
    palavras = str.split(frase)
    numerodepalavras = len(palavras)
    return numerodepalavras