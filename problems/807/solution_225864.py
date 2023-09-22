def conta_frases(text):
  """a função retorna o número de frases em um texto; str->int"""
  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')

  return quant +1