def retira_pontuacao(a):
    a = a.replace("."," ");
    a = a.replace(","," ");
    a = a.replace(":"," ");
    a = a.replace(";"," ");
    a = a.replace("!"," ");
    a = a.replace("?"," ");
    a = a.replace("..."," ");
    a = a.replace("-"," ");
    return a