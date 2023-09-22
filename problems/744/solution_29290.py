# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string que coloca o símbolo # no início,meio e fim 
    de uma string dada como entrada: str -> str"""
    a = len(s)
    b = round(a/2)
    return '#' + n[0:b] + '#' + n[b:] + '#'