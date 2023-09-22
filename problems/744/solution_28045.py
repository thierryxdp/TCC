# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao que recebe uma string e insere o caractere # no inicio. meio e final dela
    str -> str"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s