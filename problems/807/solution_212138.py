def contas_frases(texto):
    """ função que dada um texto determina o número de frases que aparcem nesse texto;
    string -> int """
    var1 = str.join("*",(str.split(texto,"...")))
    var2 = str.join("*",(str.split(var1,"?")))
    var3 = str.join("*",(str.split(var2,"!")))
    var4 = str.join("*",(str.split(var3,".")))
    var5 = str.split(var4,"*")
    return len(var5)