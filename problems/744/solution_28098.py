# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que recebe uma string e insere o caractere '#' no comeco, no meio
    e no final da mesma; str->str"""
    return '#'+str(s)[:len(s)//2]+'#'+str(s)[len(s)//2:]+'#'