def retira_pontuacao(frase):
    pont1 = "-"
    pont2 = ("."",")
    pont3 = "!"
    return str.replace(frase,pont2,' ')