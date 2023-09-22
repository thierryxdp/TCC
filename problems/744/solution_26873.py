# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string com o caractere '#' no inicio, meio e e no final dela;
       str->str
       Parâmetro:
       s: string
    """
    return '#'+s[0:2]+'#'+s[2:]+'#'