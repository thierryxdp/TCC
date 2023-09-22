def conta_frases(text):
  """a função contabiliza o numero de frases num texto; str->int"""
  quant = 0
  reticencias = 0 
  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')
  reticencias = reticencias + str.count(text, '...')
  quant  = (quant - (reticencias * 3)) + 1
  return quant