# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string que coloca o símbolo # no início,meio e fim 
    de uma string dada como entrada: str -> str"""
    a = len(s)
    b = int(a/2)
    return '#' + s[0:b] + '#' + s[b:] + '#'