def hashtag(s):
    """Retorne a string com # no inicio, meio e fim;
    string -> string"""
    metade = len(s) // 2
    return "#"+s[:metade]+"#"+s[metade:]+"#"