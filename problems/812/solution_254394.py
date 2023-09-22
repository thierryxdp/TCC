def retira_pontuacao(frase):
        
#retorna uma frase onde os caracteres de pontuação foram substituidos por espaço
        
    n = str(frase)
    n = n.replace("/", " ")
    n = n.replace(",", " ")
    n = n.replace(":", " ")
    n = n.replace(";", " ")
    n = n.replace(".", " ")

    return n