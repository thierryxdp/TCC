import string

def quant_frases(text):

  #contabliliza o numero de frases
  quant = 0
  reticencias = 0
  #soma todas as ocorrÃªncias de frases 
  quant = str.count(text, '!')
  quant = quant + str.count(text, '?')
  quant = quant + str.count(text, '.')
  reticencias = reticencias + str.count(text, '...')

  #usa-se para diminuir as vezes que o ponto Ã© contado, mas na realidade Ã© uma reticÃªncia
  quant  = (quant - (reticencias * 3)) 
  return quant