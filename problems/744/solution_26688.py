def hashtag(s):
    s = str(s)
    nome = int(len(s)/2)
    return '#'+s[0:nome]+'#'+s[nome:]+'#'