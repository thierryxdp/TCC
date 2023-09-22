# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """calcula e retorna uma string com o caractere '#' inserido em seu início, meio e fim;
    str -> str"""
    metade = len(s)//2
    return '#' + s[0:metade] + '#' + s[metade:] + '#'