def hashtag(s):
    """Adiciona uma hashtag no inicio no meio e no fim de uma string s.
    str->str
    
    Parameters:
    s= A string que vai receber as hashtags.
    
    Returns:
    A string com uma hashtag no inicio no meio e no fim da string inserida
    """
    y=len(s)//2
    return "#"+s[:y]+"#"+s[y:]+"#"