def hashtag(s):
    '''funçao que faz com que o # seja inserido no inicio, meio e fim de uma string; str->str'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'