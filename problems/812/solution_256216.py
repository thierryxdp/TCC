def retira_pontuacao (s):
    s1 = s
    s2= s.replace("-", " ")
    s2= s.replace(",", " ")
    s2= s.replace(":", " ")
    s2= s.replace(";", " ")
    s2= s.replace(".", " ")
    s2= s.replace("!", " ")
    s2= s.replace("?", " ")
    return s2