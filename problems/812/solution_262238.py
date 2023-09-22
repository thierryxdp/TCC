def retira_pontuacao(frase):
    "Retorne a dada frase substuindo suas pontuaçoes por espaços; str->str"
    x=str.replace(frase,'.',' ')
    y=str.replace(x,'.',' ')
    return x