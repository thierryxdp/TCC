def hashtag(s):
    """Dada uma String s retorma essa string com Hashtags,
    no inicio no meio e no final dela."""
    str_div = (len(s)//2) 
    marcada = str('#')+s[:str_div]+str('#')+s[str_div:]+str('#')
    return marcada