def hashtag(s):
    """retorna a string s com o caractere '#' no início, meio e no final dela
    str -> str"""
    i = len(s)
    pmetade = s[:i//2]
    smetade = s[i//2:]
    return '#' + pmetade + '#' + smetade + '#'