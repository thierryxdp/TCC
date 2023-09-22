def retira_pontuacao(frase):
    x = str.replace(frase,"!"," ")
    y = str.replace(frase,"."," ")
    z = str.replace(frase,"?"," ")
    w = str.replace(frase,"-"," ")
    a = str ("!")
    if a in frase:
        return x