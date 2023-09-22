# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função recebe como entrada uma string e retorna
    a mesma string, mas com uma hashtag no início, uma no final
    e uma no meio."""
    if len(s)%2 == 0:
        return '#' + s[:((len(s))//2)] + '#' + [((len(s))//2):] + '#'
    else:
        return '#' + s[:(len(s) - 1)