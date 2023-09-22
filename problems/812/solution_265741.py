def retira_pontuacao(s):
    a=s.replace("—"," ")
    b=s.replace(","," ")
    c=s.replace(":"," ")
    d=s.replace(";"," ")
    e=s.replace("."," ")
    return a+b+c+d+e