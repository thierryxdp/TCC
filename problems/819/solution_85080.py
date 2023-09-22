def filtraMultiplos(num, n):
listaNum = []
i = 0
while i < len(num):
if num[i]%n == 0:
listaNum.append(num[i])
i+=1
return listaNum