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
    s2 = retira_pontuacao(s1)
    ls = str.split(s2)
    list.reverse(ls)
    s3 = str.join(" ", ls)
    return s3