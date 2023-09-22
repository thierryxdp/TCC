def conta_frases(text):


  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')


  quant  = (quant - (reticencias * 3)) 
  return quant