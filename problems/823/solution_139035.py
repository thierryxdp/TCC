def faltante(L):
  '''Função que, dada uma lista L com N − 1 inteiros numerados de 1 a N, descobre qual número inteiro deste intervalo está faltando, e o retorna.
  list -> int'''
  
  list.sort(L)
  i = 0

  if 1 not in L:
    #Se 1 não estiver na lista
    return 1

  while i < len(L) - 1:
    #Enquanto o termo for um dos elementos da lista com ao menos 1 elemento a sua frente (até o penúltimo)
    if L[i] != L[i+1] - 1:
      #Se o sucessor for diferente do elemento, retorna o real sucessor
      return L[i] + 1
    i += 1
    #Contador prossegue ao próximo elemento
  return L[i] + 1
  #Se todos os elementos tiverem sucessores, retorne o sucessor do último elemento