# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    :param s: uma string
    :return: Uma uma string onde no início, meio e final tem o caracter #"""
    # s = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s