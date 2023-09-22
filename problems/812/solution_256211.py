def retira_pontuacao (s):
    
    a= s.replace("-", " ")
    a= s.replace(",", " ")
    a= s.replace(":", " ")
    a= s.replace(";", " ")
    a= s.replace(".", " ")
    a= s.replace("!", " ")
    a= s.replace("?", " ")
    return a