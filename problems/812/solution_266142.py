def retira_pontuacao(a):
    b=a.replace(".","").replace(",","").replace("!","").replace("?","").replace(":","").replace("-","").replace(";","")
    return b