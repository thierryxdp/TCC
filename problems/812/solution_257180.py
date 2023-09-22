def retira_pontuacao(x):
    w = ""
    w = x.replace("."," ")
    w = x.replace("!"," ")
    w = x.replace("?"," ")
    w = x.replace(","," ")
    w = x.replace("-"," ")
    w = x.replace(":"," ")
    w = x.replace(";"," ")
    return w