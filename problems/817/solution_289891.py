def acima_da_media(notas):
   soma = sum(notas)
   med = float(soma)/len(notas)
   list.insert(notas,-1,med)
   list.sort(notas)
   i = list.index(notas,med)
   return notas[i+1:]