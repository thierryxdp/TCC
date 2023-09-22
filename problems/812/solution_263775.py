def retira_pontuacao(frase):
    str.replace(frase,"-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ")