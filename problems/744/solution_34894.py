def hashtag(s):
    if len(str(s))%2==0:
        return '#'+str(s)[0:len(str(s))/2]+'#'+str(s)[len(str(s))/2:]+'#'
    else:
        return '#'+str(s)[0:len(str(s))/2-0.5]+'#'+str(s)[len(str(s))/2-0.5:]+'#'