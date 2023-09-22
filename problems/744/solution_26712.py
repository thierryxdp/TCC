# str-> str
def hashtag(s):
    """insere # no início, no meio e no final da string s"""
    return "#"+s[:(len(s)//2)]+"#"+s[(len(s)//2):]+"#"