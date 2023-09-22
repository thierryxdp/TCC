def conta_frases(texto):
        """A entrada será um texto contido no parâmetro
        e se retornará o número de frases contidas nele"""
        # string -> string
       
       
        texto.replace ("...", ".")
        textoreticencias = texto.replace ("...", ".")
        texto.replace ("!", ".")
        textoexclamacao = textoreticencias.replace ("!", ".")
        texto.replace ("?", ".")
        textointerrogacao = textoexclamacao.replace ("?", ".")
        textoexclamacao.split (".")
        return len (texto)