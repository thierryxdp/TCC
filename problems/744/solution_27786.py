# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """dada uma string, insere um caractere no inicio, no meio e no final dela.
    str->str"""
    u=len(s)//2
    return s[:u]+s+s[u:]