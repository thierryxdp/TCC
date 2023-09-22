def maiores(lista_numero,n):
  '''Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os números da lista original maiores que n ordenados em ordem crescente.
  list, int -> list'''

  #Cria uma lista vazia (ordenação final)
  lista_ord = []
  
  #Adiciona n e ordena a lista crescentemente
  list.append(lista_numero,n)
  list.sort(lista_numero)

  #Encontra o índice de n na nova lista
  ind = list.index(lista_numero,n)

  #Fatia a nova lista considerando os índices de n (exclusive) ao final, e adiciona o fatiamento à lista vazia
  lista_ord += lista_numero[(ind+1):]

  return lista_ord