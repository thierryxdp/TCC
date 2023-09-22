# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e a retorna com o caractere # no 
    começo, meio e fim da string."""
    n = len (s)//2
    return '#'+s[:n]+'#'+s[n:]+'#'