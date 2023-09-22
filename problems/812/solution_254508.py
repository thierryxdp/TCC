retira_pontuação(x):
    """Substitui a pontuação por um espaço vazio"""
    x=x.replace(";","#")
    x=x.replace("!","#")
    x=x.replace("?","#")
    x=x.replace(".","#")
    x=x.replace(":","#")
    x=x.replace(",","#")
    x=x.replace("...","#")
    s=str.replace(x,"#"," ")
    return s