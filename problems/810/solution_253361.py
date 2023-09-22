def retira_pontuacao(x):
    x=x.replace("!"," ")
    x=x.replace("-"," ")
    x=x.replace(","," ")
    x=x.replace(":"," ")
    x=x.replace("."," ")
    x=x.replace("?"," ")
    return x

def inverte(x):
    m= retira_pontuacao(x).lower().split()
    return m