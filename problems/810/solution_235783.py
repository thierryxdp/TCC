def inverte(frase):
    """função que recebe uma frase e retorna outra frase que contenha as mesmas palavras em ordem inversa;
       str -> str"""
    
        var1 = str.join(" ",(str.split(frase,"...")))
        var2 = str.join(" ",(str.split(var1,",")))
        var3 = str.join(" ",(str.split(var2,":")))
        var4 = str.join(" ",(str.split(var3,";")))
        var5 = str.join(" ",(str.split(var4,".")))
        var6 = str.join(" ",(str.split(var5,"-")))
        var7 = str.join(" ",(str.split(var6,"!")))
        var8 = str.join(" ",(str.split(var7,"?")))
        var9 = var8[::-1]
        var10 = str.join(" ",(var9))
        return var10