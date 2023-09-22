# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a a string s com o caractere '#' adicionado no início, no meio e no fim.
    str -> str"""
    return '#' + s[:len(s) // 2] + '#' + s[len(s) // 2:] + '#'