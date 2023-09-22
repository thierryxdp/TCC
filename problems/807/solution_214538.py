def conta_frases(frase):
    " função que coloca um texto e retorna o número de frases existentes, retirando os pontos. str --> str"
    x = str.replace(frase"...","#")
    return str.count(x".")+str.count(x,"!")+str.count(x,"?")+strcount(x,"#")