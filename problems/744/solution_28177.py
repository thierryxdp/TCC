def hashtag(s):
    """ Função que retorna uma string com # no início, meio e fim
       str->str"""
    
    meio = len(s)//2
    pos1 = str(s[:meio])
    pos2 = str(s[meio:])
    return '#'+pos1+'#'+pos2+'#'