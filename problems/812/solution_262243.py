def retira_pontuacao(frase):
    "Retorne a dada frase substuindo suas pontuaçoes por espaços; str->str"
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,'-',' ')
    w=str.replace(z,'!',' ')
    xx=str.replace(w,'?',' ')
    return xx