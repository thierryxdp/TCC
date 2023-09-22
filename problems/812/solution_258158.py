def retira_pontuacao(x):
    """substitui uma pontuaçao por espaçamento"""
    y= x.replace("."," ")
    z= y.replace("!"," ")
    w= z.replace(","," ")
    
    return z