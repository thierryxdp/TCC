def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' or '?' or '.' or '...' or ';' or '-' or ':' or ','
    y = '!','?','.','...',';','-',':',','
    frase = frase.replace('!', ' ') and frase.replace('?', ' ') and
                 frase.replace('.', ' ') and frase.replace('...', ' ') and
                 frase.replace(';', ' ') and frase.replace('-', ' ') and
                 frase.replace(':' , ' ') and frase.replace(',', ' ')
    return frase