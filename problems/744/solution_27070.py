# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e retorna uma string com o caractere '#' no inicio
       no meio e no final;
       str->str
    """
    d= int(len(s)/2)
    return '#'+s[:d]+'#'+s[d:]+'#'