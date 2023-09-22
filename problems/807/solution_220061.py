def conta_frases(texto):
        """A entrada será um texto contido no parâmetro
        e se retornará o número de frases contidas nele"""
        # string -> string
       
        textocomponto = len(str.split('.'))
        textocomexclamacao = len(str.split('!'))
        textocominterrogacao = len(str.split('?'))
       
        return texto = textocomponto + textocomexclamacao + textocominterrogacao: