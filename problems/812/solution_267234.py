def retira_pontuacao(x):
    x=x.replace("!"," ")
    x=x.replace("-"," ")
    x=x.replace(","," ")
    x=x.replace(":"," ")
    x=x.replace("."," ")
    return x