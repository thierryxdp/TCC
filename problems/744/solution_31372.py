# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """função que recebe uma string e retorna a mesma string
    com o caractere "#" no inicio, no meio e no final dela
    str -> str"""
    comeco = len(s)//2
    final = -len(s)//2
    return s