def retira_pontuacao(ponto):
    a = ponto
    b = "!@#$"
    for char in b:
        a = a.replace(char,"")

           print (a)