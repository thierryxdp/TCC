def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    nova_frase = frase.replace(',' and '.',' ')
    return nova_frase