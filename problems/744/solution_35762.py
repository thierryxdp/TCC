def hashtag (string):
    '''função que insere # no início, no meio e no final da string'''
    
hashtag = '#'+string+'#'
meio = len(string)//2
hashtag = string[:meio] + '#' + string[meio:]
    return hashtag