def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' or '?' or '.' or '...' or ';' or '-' or ':' or ','
    y in '!?.;:,-'
    if y in frase:
    frase = frase.replace(y, ' ')
    return frase