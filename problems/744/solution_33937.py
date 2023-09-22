def hashtag(s):
    """coloca uma hastag no inicio, meio e final de uma string,
    string -> string"""
    return "#"+s[0:len(s)//2]+"#"+s[len(s)//2:]+"#"