def hashtag(s):
    """."""
    inicio = '#' + s [0]
    meio = '#' + str (len (s) // 2) 
    fim = s [-1] + '#'
    return  inicio + meio + fim