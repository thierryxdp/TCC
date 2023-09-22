def retira_pontuacao(frase):
    """str -> str; 
    Função que, dada uma frase, retorna ela porém com ' ' no
    lugar de todos os caracteres de pontuação."""
    s = '!?;,-.:'
    for x in s:
        frase = frase.replace( x , ' ')
    return frase