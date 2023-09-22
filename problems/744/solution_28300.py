# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e retorna essa string com '#' no início, no meio e no final dela; str -> str. """
    meio = len(s)//2
    return '#'+s[:meio]+'#'+s[meio:]+'#'