def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    y = '.'
    #x = '!' and '?' and ';' and '-' and ':' and ','
    x =','
    l = ['!','?',';',':',',','-']
    s = '!?;,-.:'
    frase = frase[:-1]
    frase = frase.replace( x , ' ')
    return frase