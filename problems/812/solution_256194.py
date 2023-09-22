def retira_pontuacao (s):
    s1 = s
    a= s1.replace("-","")
    b= s1.replace(",", "")
    c= s1.replace(":", "")
    d= s1.replace(";", "")
    return a+b+c+d