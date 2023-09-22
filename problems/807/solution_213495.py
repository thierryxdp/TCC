def conta_frase (texto):
    """Função que retorna o número de frase que aparece num determinado texto"""
    #string -> int
    texto_dividido = texto.count ("!") 
    texto_dividido = texto.count ("?")
    texto_dividido = texto.count (":")
    frase = len (texto_dividido) 
    return frase