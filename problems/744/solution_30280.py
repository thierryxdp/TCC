def hashtag(s):
    """recebe uma string e retorna essa mesma string, mas com # em seu inicio, meio e final"""
    
    x = len(s)
    y = (x / 2)
    y = int y
    
    s1, s2 = s[:y], s[y:]
    
    return '#' + s1 + '#' + s2 + '#'