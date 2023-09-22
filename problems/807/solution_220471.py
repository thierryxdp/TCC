def conta_frases(texto):
        """A entrada será um texto contido no parâmetro
        e se retornará o número de frases contidas nele"""
        # string -> string
       
        numerofrases = 0
        texto = texto.replace ("...", ".")
        numerofrases += texto.count (".")
        numerofrases += texto.count ("!")
        numerofrases += texto.count ("?")
        numerofrases += texto.count ("...")
        
        texto.split ()
        return len (texto)