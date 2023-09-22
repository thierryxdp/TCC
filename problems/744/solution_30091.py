def hashtag(s):
    x=s
    y=len(x)
    z=int((y//2))
    return '#'+x[0:z]+'#'+x[z:]+'#'