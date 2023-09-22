def frases(K):
  pontos_e_retic = K.count('.') 
  excl           = K.count('!')
  interr         = K.count('?')
  retic          = K.count('...')
  pontos         = pontos_e_retic - 3*retic

  return (excl+interr+retic+pontos)