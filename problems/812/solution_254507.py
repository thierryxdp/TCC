retira_pontuação(x):
    """Substitui a pontuação por um espaço vazio"""
    y=str.replace(x,","," ")
    z=str.replace(y,"."," ")
    a=str.replace(z,"?"," ")
    b=str.replace(a,"!"," ")
    c=str.replace(b,"-"," ")
    d=str.replace(c,"..."," ")
    return d