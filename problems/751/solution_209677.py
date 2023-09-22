def quant_palavras(frase):
    """Essa função retorna quantas palavras existem 
    em uma frase informada 
    string -> int"""
    
    return len(str.split(str.strip(frase," ")," "))