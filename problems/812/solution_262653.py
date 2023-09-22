def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    pontuacao = [".",",",":",":",";","?","!"]
    nova_frase = frase.replace('pontuacao',' ')
    return nova_frase