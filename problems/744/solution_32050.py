def hashtag(s):
    """coloca uma hashtag no inicio, meio e fim de uma string;
    str -> str"""
    return '#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2) :] + '#'