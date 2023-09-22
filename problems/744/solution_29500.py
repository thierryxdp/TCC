def hashtag(s):
    """recebe uma string e insere o # no inicio, meio e final"""
    
    meio = len(s)//2
    
    return '#'+str(s([0:meio)])+'#'+str(s([meio:]))+'#'