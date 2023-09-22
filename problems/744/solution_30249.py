def hashtag(s):
    """retorna # no ínicio, meio e final de uma string. str-> str"""
    if len(s) == 4:
        return '#' + s[0:4] + '#' + s[4:] + '#'
    
    elif len(s) == 3:
        return  '#' + s[0:3] + '#' + s[3:] + '#'