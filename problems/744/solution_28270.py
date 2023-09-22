# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao que recebe uma string e insere o caractere '#' no inicio, meio e fim dela"""
    """str -> str"""
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'