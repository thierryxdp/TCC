def retira_pontuacao(x=""):
    x=x.replace(".","").replace(";","").replace(",","").replace("-"," ").replace(":","").replace("?","").replace("!","").replace("/","")
    return x

def inversa(x=""):
    x=retira_pontuacao(x).lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])