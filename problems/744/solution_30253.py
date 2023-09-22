def hashtag(s):
    """retorna # no ínicio, meio e final de uma string. str-> str"""
    if len(s) == 8:
        return '#' + s[0:4] + '#' + s[4:] + '#'
    
    elif len(s) == 9:
        return  '#' + s[0:3] + '#' + s[3:] + '#'
    
    elif len(s) == 10:
        return  '#' + s[0:5] + '#' + s[5:] + '#'