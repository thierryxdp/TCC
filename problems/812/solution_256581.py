def retira_pontuacao (p) :
    p1= p.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")
    return p1