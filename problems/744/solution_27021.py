# Coloque um comentário dizendo o que a função faz
def hashtag(s):
    """Função chamada hashtag que recebe uma string e insira o caractere 
    ”#” no in ́ıcio, no meio e no final dela.
    str -> str
    """
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'