# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que insere # no início/meio/fim."""
    return "#" + s[0:(len(s)//2)] + "#" + s[(len(s)//2):-1] + "#"