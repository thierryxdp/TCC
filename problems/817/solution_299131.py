def maiores(numeros,n):
   list.append(numeros, n)
   list.sort(numeros)
   return numeros[numeros.index(n)+1:]
   
def acima_da_media(notas):
   media = sum(notas)/len(notas)
   media = int(media) + 1
   return maiores(notas,media)