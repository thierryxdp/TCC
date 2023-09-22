def medTurma (notas):
   
   soma = sum(notas)
   n = len(notas)
   med = float(soma)/n
   
   list.insert(notas,-1,med)
   list.sort(notas)
  
   i = list.index(notas,med)
   
   return notas[i+1 :]