# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função para inserir o simbolo da hashtag numa string.
       Onde: "s" - é a string que será modificada.
    str -> str"""
    posicao = len(s) // 2
    antes = s[:posicao]
    depois = s[posicao:]
    return "#" + antes + "#" + depois + "#"