def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = ('!' and '?' and ';' and '-' and ':' and ',' and '.')
    l = ['!','?',';',':',',','-']
    s = '!?;,-.:'
    while x in s
       frase = frase.replace( x , ' ')
    return frase