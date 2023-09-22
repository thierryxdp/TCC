def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' and '?' and '.' and '...' and ';'and '-' and ':' and ','
    y = '!' or '?' or '.' or '...' or ';'and '-' or ':' or ','
    if y in frase:
        frase = frase.replace(y, ' ')
    return frase