def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' or '?' or '.' or '...' or ';' or '-' or ':' or ','
    l = ['!','?',';',':',',','-']
    if l[i] in frase:
    frase = frase.replace(x, ' ')
    return frase