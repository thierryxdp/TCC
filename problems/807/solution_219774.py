def conta_frases(texto):
        """A entrada será um texto contido no parâmetro
        e se retornará o número de frases contidas nele"""
        # string -> string
       
        textocomponto = len(str.split('.'))
        textocomexclamacao = len(str.split('!'))
        textocominterroacao = len(str.split('?'))
        textocomreticencias = len(str.split('...'))
        return texto = textocomponto + textocomexclamacao + textocominterrogacao + textocomreticencias:
        if (textocomponto == '.'):
            texto = texto - 1