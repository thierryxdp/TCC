# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Insere uma # no início, no meio e no final de uma string
       Dados de entrada: s --> string entre aspas"""
    a = len(s)
    return "#" + s[0:a//2] + "#" + s[a//2:] + "#"