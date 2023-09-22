def hashtag(s):
'''recebe uma string, encontra seu meio e coloca uma hashtag no seu inicio meio e fim
    str -> str'''
    l = len(s)
    return "#" + s[0:2//2] + "#" + s[l//2:] + "#"