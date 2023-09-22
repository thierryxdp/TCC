def freq_palavras(frases):
   lista = []
   lista = frases.split()
   frequ = [lista.count(p) for p in lista]
   return (dict(zip(lista,frequ)))