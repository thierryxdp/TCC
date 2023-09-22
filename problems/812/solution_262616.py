def retira_pontuacao(frase):
    """Função que dada frase, a retorna com suas pontuações substituídas por espaço;
    str -> str"""
    return string.replace(frase, ('.','-',';',':',','),' ')