def retira_pontuaçao(frase):

    x = str.replace(frase,'.',' ')
    y = str.replace(x,',',' ')
    z = str.replace(y,'-',' ')
    w = str.replace(z,':',' ')
    a = str.replace(w,';',' ')
    return a