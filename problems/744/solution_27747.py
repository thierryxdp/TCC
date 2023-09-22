def hashtag(s):
    """A funçao retorna a string com # entre as letras da string 
    str-> str"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s