def retira_pontuacao(f):
    "str-->str"
    
    f1= str.replace(f,"-"," ")
    f2= str.replace(f1,","," ")
    f3= str.replace(f2,":"," ")
    f4= str.replace(f3,";"," ")
    return f4