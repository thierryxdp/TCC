# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Essa funcao insere uma "x" no inicio meio e final de uma string dada
    """
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'