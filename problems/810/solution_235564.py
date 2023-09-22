def inverte(s0):
    "dada uma frase, retorna-a invertida, sem sinais de pontuações ou diferenciação de caixa alta ou baixa. str -> str"
    a = str.replace(s0,"."," ")
    b = str.replace(a,","," ")
    c = str.replace(b,"-"," ")
    d = str.replace(c,"!"," ")
    e = str.replace(d,"?"," ")
    f = str.replace(e,":"," ")
    g = str.replace(f,";"," ")
    s1 = str.split(g)
    s2 = s1[::-1]
    return str.lower(str.join(" ", s2))