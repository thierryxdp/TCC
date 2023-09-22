def hashtag(s):
    """divide a string e adiciona #s no inicio, meio e fim"""
    s1 = [len(s)//2:]
    s2 = [:len(s)//2]
    return '#' + s1 + '#' + s2 + '#'