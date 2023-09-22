import math 
def hashtag(s):
    """Função que da uma string retorna um caractere '#' no início, no meio
    e no final dela;
    str -> str"""
    n = math.floor(len(s)/2)
    return "#"+s[0:n]+"#"+s[n:]+"#"