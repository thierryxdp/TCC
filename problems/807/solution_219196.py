def conta_frases (x):
    " A função recebe um frase "
    " As funções de y a t, pegam os pontos finais e mudam para *"
    y = x.replace("!","*")
    k = y.replace(".","*")
    t = k.replace("?","*")
    " Posteriomente a frase e separada a cada *, formando frases separadas"
    o = str.split(t,"*")
    " Esse artificio e usado devido, a ficar um parte a mais da função o"
    d = len(o)-1
    return d