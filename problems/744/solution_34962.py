def hashtag(s):
    if len(str(s))%2==0:
       
        return '#'+str(s)[0:int(len(s)/2)]+'#'+str(s)[int(len(s)/2):]+'#'