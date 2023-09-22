def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    if ('.') in frase == True:
    nova_frase = frase.replace('.',' ')
    return nova_frase