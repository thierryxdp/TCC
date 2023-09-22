def maiores(numeros,n):
   numeros.append(n)
   list.sort(numeros)
   return numeros[n+1:]
   
def acima_da_media(notas):
   media = sum(notas)/len(notas)
   media = int(media)
   return maiores(notas,media)