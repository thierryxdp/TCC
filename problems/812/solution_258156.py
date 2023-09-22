def retira_pontuacao(x):
    """substitui uma pontuaçao por espaçamento"""
    y= x.replace("."," ") + x.replace("!"," ") + x.replace("?"," ") +x.replace("-"," ")+x.replace(":"," ")+x.replace(";"," ")+x.replace(","," ")
    return y