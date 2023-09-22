def conta_frases(text):
  """a função retorna o número de frases em um texto; str->int"""
  quant = 0
  reticencias = 0 
  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')

  return quant