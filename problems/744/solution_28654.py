def hashtag(s):
    """a função colocará '#' no começo, meio e fim na string escolhida
    pelo usuário.
    Entrada: string
    Saída: string"""
    s1 = len(s)//2
    s2 = s[:s1]
    s3 = s[s1:]
    return '#' + s2 + '#' + s3 + '#'