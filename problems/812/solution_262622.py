def retira_pontuacao(frase):
    """Função que dada frase, a retorna com suas pontuações substituídas por espaço;
    str -> str"""
    nova_frase = frase.replace("'.','-',';',':',','",' ')
    return nova_frase