def retira_pontuacao(frase): #not in ("""ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç""")
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    x = '!' and '?' and '.' and '...' and ';'and '-' and ':' and ','
    y = '!','?','.','...',';','-',':',','
    frase = frase.strip('.')
    if x in frase:
        frase = (frase.replace('!', ' ') and frase.replace('?', ' ') and
                 frase.replace('.', ' ') and frase.replace('...', ' ') and
                 frase.replace(';', ' ') and frase.replace('-', ' ') and
                 frase.replace(':' , ' ') and frase.replace(',', ' '))
    return frase