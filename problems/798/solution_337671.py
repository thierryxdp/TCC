def freq_Palavras(frases):
   palavras = frases.split(' ')
   dictResult = dict()
   for palavra in palavras:
      if palavra in dictResult:
         dictResult[palavra] += 1
      else:
         dictResult[palavra] = 1
   return dictResult