def conta_frases(frase):
  '''função que dado um texto armazenado em uma string, retorna quantos números de frases aparecem no texto,sendo que
     cada frase no texto é terminada com um ponto final(.), um ponto de exclamação(!), um ponto de interrogação(?) ou
     três pontos em sequência(reticências). Pontos de exclamação ou de interrogação não aparecerão repedidos em sequência
     no texto e esses símbolos só aparecem no texto terminando uma frase;
     str -> str'''
   frase = str.count(".")
    return len(frase)