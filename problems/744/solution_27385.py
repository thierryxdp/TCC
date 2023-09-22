# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que dada uma string s, coloca o caractere "#" no inicio, no meio e no final dela.
    str -> str"""
    return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:] + "#"