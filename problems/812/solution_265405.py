def retira_pontuacao (frase):
    x = str.replace(frase,'.' , ' ')
    y = str.replace(x,',', ' ')
    z = str.replace(y,'!', ' ')
    t = str.replace(z,'-', ' ')
    return  t