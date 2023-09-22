def retira_pontuacao(frase):
    f1=frase.replace("-"," ")
    f2=f1.replace(","," ")
    f3=f2.replace(":"," ")
    f4=f3.replace(";"," ")
    f5=f4.replace("."," ")
    return f5