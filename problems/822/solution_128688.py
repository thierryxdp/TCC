def repetidos(num):
  '''funçao que ,dada uma lista de numeros,
  retorna o número de  vezes que um elemento 
  da lista é igual ao elemento anterior.  
  list->int'''
i=0
vzs=0
while 0<i<len(num):
    if num[i]==num[i-1]:
        vzs=vzs+1
    i=i+1
return vzs