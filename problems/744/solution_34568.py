def hashtag(s):
    """Função que recebe uma string e que retorne com '#' no inicio
    meio e fim dela.
    str -> str"""
    pre = s[:len(s)//2]
    pos = s[len(s)//2:]
    s = '#' + pre + '#' + pos + '#'
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s