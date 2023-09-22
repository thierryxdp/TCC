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
        tamanho = tamanho//2
        return a + s[:tamanho] + a + s[tamanho:] + a
    else:
        return '#' + s[:(len(s) - 1)