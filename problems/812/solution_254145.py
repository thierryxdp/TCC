def retira_pontuacao(frase):
    """função que dada uma frase, retorna a mesma função só que com todos as pontuações substítuidas por espaço;
    string -> string"""
    var1 = str.join(" ",(str.split(frase,"...")))
    var2 = str.join(" ",(str.split(var1,",")))
    var3 = str.join(" ",(str.split(var2,":")))
    var4 = str.join(" ",(str.split(var3,";")))
    var5 = str.join(" ",(str.split(var4,".")))
    var6 = str.join(" ",(str.split(var5,"-")))
    var7 = str.join(" ",(str.split(var6,"!")))
    var8 = str.join(" ",(str.split(var7,"?")))               
    return var8