#frase termina com . ou ! ou ? ou ,
    def conta_frases(texto):
        caso1 = str.split(texto, ",")
        caso2 = str.split(caso1, ".")
        caso3 = str.split(caso2, "!")
        caso4 = str.split(caso3, "?")
        return str.count(caso4)