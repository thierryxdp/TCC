def retira_pontuacao (frase):
    f1 = str.replace (' - ', " ")
    f2 = str.replace (' , ', " ") 
    f3 = str.replace (' : ', " ")
    f4 = str.replace (' ; ', " ")
    f5 = str.replace (' . ', " ")
    return f1 + f2 + f3 + f4 + f5