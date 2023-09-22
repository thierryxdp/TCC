def retira_pontuacao(x):
    x=x.replace("!"," ")
    x=x.replace("-"," ")
    x=x.replace(","," ")
    x=x.replace(":"," ")
    x=x.replace("."," ")
    x=x.replace("?"," ")
    return x

def inverte(x):
    return retira_pontuacao(x).lower().split().reverse()