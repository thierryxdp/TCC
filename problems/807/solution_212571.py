def conta_frase (texto):
     """Função que retorna o número de frase que aparece num determinado texto"""
     #string -> int
    texto_dividido = texto. replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("-"," ")  
    len (texto_dividido)
    return texto