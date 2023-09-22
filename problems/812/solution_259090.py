def retira_pontuacao(s):
    
    if(str.count(s, '... ')>0):
        s = str.replace(s, , " ")
    elif(str.count(s, ', ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, '! ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, '? ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, ': ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, '; ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, '| ')>0):
         s = str.replace(s, , " ")
    elif(str.count(s, '. ')>0):
         s = str.replace(s, , " ")
    else:
         return s
    return s