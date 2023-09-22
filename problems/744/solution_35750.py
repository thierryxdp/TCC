# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(texto):
    """recebe uma string e insira o caractere ”#” no início, no meio e no final dela, str->str"""
    from math import floor
    meio= floor(len(texto)/2)
    return '#'+texto[0:meio]+'#'+texto[meio:]+'#'