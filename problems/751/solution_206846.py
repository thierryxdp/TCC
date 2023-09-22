def quant_palavras(frase):
    """retorna quantas palavras a string fornecida tinha.
    string -> int"""
    # string -> int
    qnt_palavras = 0
    for " " in frase[0:]:
        qnt_palavras +=1
    return qnt_palavras