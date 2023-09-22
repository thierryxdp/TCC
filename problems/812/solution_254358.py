def retira_pontuaçao(frase):
    for n, i in enumerate(frase):
        if i == "?":
            frase[n] = " "
            
             return frase