def quant_frases(text):
"""a funçao retorna o número de frases de um texto; str->int""" 
  quant = 0
  reticencias = 0
  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')
  reticencias = reticencias + str.count(text, '...')
  quant  = (quant - (reticencias * 3)) + 1
  return quant