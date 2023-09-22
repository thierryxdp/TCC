def hashtag(s):
    """ Molda a string s para que no começo ela tenha "#", no meio e no final;
    str -> str"""
    return "#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"