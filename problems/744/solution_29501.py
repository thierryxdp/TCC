def hashtag(s):
    """recebe uma string e insere o # no inicio, meio e final"""
    
    meio = len(s)//2
    
    return '#'+s([0:meio)])+'#'+s([meio:]+'#'