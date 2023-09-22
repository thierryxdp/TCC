def hashtag(s):
    """função para adicionar '#' no início, no meio e no fim da string"""
    """string -> string"""
    antes = s [:len(s)//2]
    depois = s [len(s)//2:]
    s = '#' + antes + '#' + depois + '#'
    return s