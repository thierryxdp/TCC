def hashtag(s):
    if len(s)%2==0:
        return '#'+str(s)[0:len(str(s))/2]+'#'+str(s)[len(str(s))/2:]+'#'