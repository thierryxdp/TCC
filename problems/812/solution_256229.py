def retira_pontuacao (s):
    s1= s.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?"," ")
    return s1