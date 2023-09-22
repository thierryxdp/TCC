def retira_pontuacao(frase):
    pont1 = "-"
    pont2 = "."
    pont3 = "!"
    frase1 = str.replace(frase,pont2,' ')
    frase2 = str.replace(frase1,pont1,' ')