def hashtag(s):
    """."""
    inicio = s [0: (len (s) // 2)] 
    meio = s [(len (s) // 2):] 
    return  '#' + str (inicio) + '#' + str (meio)  + '#'