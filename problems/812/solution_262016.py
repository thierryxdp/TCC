def retira_pontuacao(texto):
    texto1 = str.replace(texto,"..."," ")
    texto2 = str.replace(texto1,"."," ")
    texto3 = str.replace(texto2,"?"," ")
    texto4 = str.replace(texto3,"!"," ")
    texto5 = str.replace(texto4,","," ")
    texto6 = str.replace(texto5,";"," ")
    texto7 = str.replace(texto6,":"," ")
    texto8 = str.replace(texto7,"-"," ")    
    
    return texto8