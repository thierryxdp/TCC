# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função recebe como entrada uma string e retorna
    a mesma string, mas com uma hashtag no início, uma no final
    e uma no meio."""
    a = '#'
    len(s) = tamanho
    if tamanho%2 == 0:
        return a + s[:(tamanho//2)] + a + [tamanho//2:] + a
    else:
        return '#' + s[:(len(s) - 1)