def retira_pontuacao(frase):
    pont1 = "-"
    pont2 = "."
    pont3 = "!"
    pont4 = ","
    frase1 = str.replace(frase,pont1,' ')
    frase2 = str.replace(frase1,pont2,' ')
    frase3 = str.replace(frase2,pont3,' ')
    return frase3