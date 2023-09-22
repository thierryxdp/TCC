def retira_pontuacao(frase):
    """str -> str;
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' or '?' or '. ' or '...' or ';' or '-' or ':' or ','
    y = ';' or '-' or ':' or ','
    if x in frase: #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç"""):
        frase.replace(x,' ')
    return frase