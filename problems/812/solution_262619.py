def retira_pontuacao(frase):
    """Função que dada frase, a retorna com suas pontuações substituídas por espaço;
    str -> str"""
    import string
    return string.replace(frase, "'.','-',';',':',','",' ')