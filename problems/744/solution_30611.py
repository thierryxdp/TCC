def hastag(s):
    """ Função que coloca hashtag
    str -> str """
    n= len(s)//2 
    frasehast='#' + s[:n] + '#' + s[n:] + '#'
    return frasehast