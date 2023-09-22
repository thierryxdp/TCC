# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna uma string s com o caractere hashtag no começo,
    no meio e no fim"""
    return '#' + s[0:(int((len(s))/2))] + '#' + s[(int((len(s))/2)):len(s)] + '#'