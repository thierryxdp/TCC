def retira_pontuacao (s):
    a= str.replace(s,"-"," ")
    b= str.replace(s,","," ")
    c= str.replace(s,":"," ")
    d= str.replace(s,";"," ")
    return a+b+c+d