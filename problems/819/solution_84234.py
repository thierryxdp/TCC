def filtraMultiplos(lista_numeros,n):
  '''Função que, dada uma lista de números e um número n, retorna outra lista que contenha todos os elementos da lista original divisíveis por n
  list, int > list'''

  divisiveis = []
  i = 0
  
  while i < len(lista_numeros):
    '''A função analisa todos os elementos da lista enquanto o iterador for menor que o tamanho da lista'''

    if lista_numeros[i] % n == 0:
      #Se o resto da divisão por n for nulo, n será um divisor do número
      divisiveis += lista_numeros[i]
      #Acrescenta o número na lista de números divisíveis
    i += 1

  return divisiveis