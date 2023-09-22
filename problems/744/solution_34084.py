# """dada a funcao retornar a hashtag no inicio,meio,fim da entrada"""
def hashtag(s):
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2:]+'#'