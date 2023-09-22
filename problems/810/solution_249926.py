def retira_pontuacao(s):
    s1 = str.replace(s, "-", " ")
    s2 = str.replace(s1, ",", " ")
    s3 = str.replace(s2, ":", " ")
    s4 = str.replace(s3, ";", " ")
    s5 = str.replace(s4, ".", " ")
    s6 = str.replace(s5, "!", " ")
    s7 = str.replace(s6, "?", " ")
    return s7

def inverte(s):
    """
"""
    s1 = str.lower(s)
    ls = str.split(s1)
    list.reverse(ls)
    s2 = str.join(" ", ls)
    s3 = retira_pontuacao(s2)
    return s3