def hashtag(s):
    """Recebe uma string e coloca "#" no início, meio e fim dela
    	str -> str"""
    x = len(s)
    y = x//2
    return '#'+s[0:y]+'#'+s[y:]+'#'