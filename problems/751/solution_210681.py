def quant_palavras(frase):
    """Dado o parâmetro frase, a função deve retornar
    a quantidade de palavras que tem na frase;
    string -> int"""
    
    numero_de_palavras=len(str.split(frase))
    
    return numero_de_palavras