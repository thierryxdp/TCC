def acima_da_media(notas):
   soma = sum(notas)
   n = len(notas)
   med = int(soma)/n
   list.insert(notas,-1,med)
   list.sort(notas)
   i = list.index(notas,med)
   return notas[i+1 :]