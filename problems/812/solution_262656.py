def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    print frase.replace('.', '  ').replace(',', '  ')