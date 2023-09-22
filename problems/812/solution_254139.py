def retira_pontuacao(f):
    b= ".,!;"
    for char in b:
        f=f.replace(char,"")
    return str(f)