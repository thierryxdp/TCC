def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' and '?' and '.' and '...' and ';'and '-' and ':' and ','
    z = '!' and '?' and '.' and '...' and ';'and '-' and ':' and ','
    y = ('!','?','.','...',';','-',':',',')
    if x in frase:
        frase = frase.replace(x, ' ')
    if z in frase:
        frase = frase.replace(z, ' ')
    return frase