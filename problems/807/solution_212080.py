def conta_frase (texto):
  """Função que retorna o número de frase que aparece num determinado texto"""
  #string -> int
    texto_dividido = texto. strip ().split (" ")  
    frase = len (texto_dividido)
    return frase