def conta_frases(text):

  quant = 0
  reticencias = 0

  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')


  quant  = (quant - (reticencias * 3)) 
  return quant