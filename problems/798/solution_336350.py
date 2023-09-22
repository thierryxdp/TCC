def freq(a):
   lista = []
   lista = a.split()
   frequ = [lista.count(p) for p in lista]
   return (dict(zip(lista,frequ)))