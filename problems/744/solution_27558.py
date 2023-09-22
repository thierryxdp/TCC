# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que insere o caractere # no início, meio e no 
    final de uma string. str -> str"""
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'