def retira_pontuacao(s):  
    for c in string.punctuation:
        s=s.replace(c,"")
    return s