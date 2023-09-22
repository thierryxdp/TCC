def freq_palavras(frase):
   '''Retorna um dicionário com as palavras da frase e quantas vezes elas
      aparecem na frase
      str -> dict'''
   palavras = frase.split()
   listaIntermediaria = []
   i = 0
   contador = 0

   while i < len(palavras):
      if palavras[i] not in listaIntermediaria:
         contador = palavras.count(palavras[i])
         listaIntermediaria.append((palavras[i],contador))
      contador = 0
      i += 1

   frequencia = dict(listaIntermediaria)

   return frequencia