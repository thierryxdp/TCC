def faltante(L):
  '''Função que, dada uma lista L com N − 1 inteiros numerados de 1 a N, descobre qual número inteiro deste intervalo está faltando, e o retorna.
  list -> int'''

  largura_lista = max(L) - 1
  list.sort(L)
  i = 0
  #Contador

  while i < largura_lista:
    if largura_lista == 1:
      #Se a lista tiver apenas uma peça
      if L[0] == 1:
        #Se a peça for a primeira peça
        return int(L[0] + 1)
      else:
        #Se a peça não for a primeira peça
        return int(L[0] - 1)
    if L[i+1] == (int(L[i]) + 1):
      #Se o algarismo consecutivo for igual ao antecedente + 1
      i += 1
      if L[-1] == max(L):
        #Se todos os algarismos tiverem consecutivos e o último algarismo for o máximo da lista, a peça faltante é a consecutiva da última
        return int(L[-1] + 1)
    else:
    #Se qualquer algarismo consecutivo não for igual ao seu antecedente + 1, acrescente o algarismo consecutivo entre esses 2
      return int(L[i] + 1)
      i += 1