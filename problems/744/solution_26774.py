def hashtag(s):
    """Dado uma string, a função retorna a mesma string com o # no inico, meio e fim dela;
    str->str"""
    return "#"+s[0:(len(s)//2)]+"#"+s[(len(s)//2):]+"#"