def retira_pontuacao(s):

    s=s.replace(","," ")

    s=s.replace("."," ")

    s=s.replace("?"," ")

    s=s.replace("!"," ")

    s=s.replace("-"," ")

    return s

def inverte(s):

    l=s.split
    l.reverse
    Return l.str