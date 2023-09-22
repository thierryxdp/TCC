def hashtag(s):
    if len(str(s))%2==0:
        return '#'+str(s)[0:len(s)-1]