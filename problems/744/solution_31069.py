def hashtag(s):
    '''faz com que # seja posto no inicio, meio e fim 
    de uma string ex: #ab#cd#'''
    primeiraParteString=s[0:(len(s)//2)]
    segundaParteString=s[int(len(s)/2):len(s)]
    return '#'+primeiraParteString+'#'+segundaParteString+'#'