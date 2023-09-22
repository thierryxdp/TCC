def retira_pontuacao(frase):
    "retira todos os caracteres de pontuação e substitui por espaço. str->str"
    a = frase.replace("-"," ")
    b = a.replace(","," ")
    c = b.replace(":"," ")
    d = c.replace(";"," ")
    e = d.replace("..."," ")
    f = e.replace("."," ")
    g = f.replace("?"," ")
    h = g.replace("!"," ")
    return h