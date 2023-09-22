def filtraMultiplos(numero, n):
listaNum = []
i = 0
while i < len(numero):
if numero[i]%n == 0:
listaNum.append(numero[i])
i+=1
return listaNum