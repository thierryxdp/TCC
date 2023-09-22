def retira_pontuacao(frase):
    """retorna a frase substituindo os caracteres de pontuacao por espaco"""
    'pontuacao' = '-',',',':',';',.'
    return str.split(frase, 'pontuacao')