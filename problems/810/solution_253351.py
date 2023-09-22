def retira_pontuacao(x):
    x=x.replace("!"," ")
    x=x.replace("-"," ")
    x=x.replace(","," ")
    x=x.replace(":"," ")
    x=x.replace("."," ")
    x=x.replace("?"," ")
    return x

def inverte(x):
    return str.lower(retira_pontuacao(x).reverse)