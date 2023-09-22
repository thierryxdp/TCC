def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    y = '.'
    #x = '!' and '?' and ';' and '-' and ':' and ','
    x =','
    l = ['!','?',';',':',',','-']
    if x and y in frase:
        frase = frase.replace(y and x , ' ')
    return frase