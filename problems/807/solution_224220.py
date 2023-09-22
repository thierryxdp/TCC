#frase termina com . ou ! ou ? ou ,
    def conta_frases(t):
        caso1 = str.split(t, ",")
        caso2 = str.split(caso1, ".")
        caso3 = str.split(caso2, "!")
        caso4 = str.split(caso3, "?")
        return str.count(caso4)