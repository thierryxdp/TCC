def retira_pontuacao(frase):
    """Troca pontuações por espaços numa frase. str->str"""
    if(str.count(frase,"!")>0):
        return str.replace(frase,"!"," ")
    elif(str.count(frase,"?")>0):
        return str.replace(frase,"?"," ")
    elif(str.count(frase,"-")>0):
        return str.replace(frase,"-"," ")
    elif(str.count(frase,", ")>0):
        return str.replace(frase,", "," ")
    elif(str.count(frase,":")>0):
        return str.replace(frase,":"," ")
    elif(str.count(frase,";")>0):
        return str.replace(frase,";"," ")
    elif(str.count(frase,".")>0):
        return str.replace(frase,"."," ")