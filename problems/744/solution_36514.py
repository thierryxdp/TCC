def hashtag(s):
    """Função que recebe uma string, e põe uma hashtag no seu inicio, no seu meio e no seu fim. str -> str"""
    l = len(s)
    return "#" + s[0:l//2] + "#" + s[l//2:] + "#"