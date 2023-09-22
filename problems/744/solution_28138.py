def hashtag(s):
    """funcao que retorna uma string com # no inicio, meio e fim dela;
    str -> str"""
    
    meio = len(s)//2
    meio1 = meio+1
    pos1 = str(s[:meio1])
    pos2 = str(s[meio:])
    return '#'+pos1+'#'+pos2+'#'