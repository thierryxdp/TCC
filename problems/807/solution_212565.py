def conta_frase (texto):
     """Função que retorna o número de frase que aparece num determinado texto"""
     #string -> int
    texto_dividido = texto. replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("-"," ")  
    frase = len (texto_dividido)