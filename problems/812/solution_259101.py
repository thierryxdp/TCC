def retira_pontuacao(s):
    
    s = s + " "
    
    if(str.count(s, '...')>0):
        s = str.replace(s,"..." , "")
    elif(str.count(s, ', ')>0):
        s = str.replace(s,"," , " ")
    elif(str.count(s, '!')>0):
        s = str.replace(s,"!" , "")
    elif(str.count(s, '?')>0):
        s = str.replace(s,"?" , "")
    elif(str.count(s, ':')>0):
        s = str.replace(s,":" , "")
    elif(str.count(s, ';')>0):
        s = str.replace(s,";" , "")
    elif(str.count(s, '|')>0):
        s = str.replace(s,"|" , "")
    s1 = s
    elif(str.count(s1, '.')>0):
        s1 = str.replace(s1,"." , "")
    elif(str.count(s1, "-")>0):
        s1 = str.replace(s1,"-" , " ")
    else:
         return s
    return s