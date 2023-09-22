def conta_frases(texto):
        """A entrada será um texto contido no parâmetro
        e se retornará o número de frases contidas nele"""
        # string -> string
       
        textocomponto = conta_frases(".")
        textocomponto.replace ("...", ".")
        textocomponto.replace ("!", ".")
        textocomponto.replace ("?", ".")
        textocomponto.split (".")
        return len (textocomponto)