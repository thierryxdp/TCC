def hashtag(s):
    """A função retorna uma string com os caracteres '#' no início, meio e fim;
str -> str"""
    return "#"+s[0:len(s)//2]+"#"+s[len(s)//2:]+"#"