def hashtag(str):
    """Recebe uma string e insere o caracte # no início, meio e fim
    dela.
    Entrada: string
    Saída: string
    """
    from math import floor
    
   
    
    if len(str)%2 == 0:
        return '#'+str[:len(str)/2-1] + '#' + str[len(str)/2-1:]+'#'
    else:
        return '#' + str[:floor(len(str)/2-1)] + '#' + str[floor(len(str)/2-1):] + '#'