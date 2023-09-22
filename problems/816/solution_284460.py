def compara_lista(lista_numero, n):
  """função que retorna uma lista de numeros inteiros em ordem crescente, maiores que um dado valor n; list,int->list"""
  nova_lista = []
  for i in range(len(lista_numero)):
    if(lista_numero[i] > n):
      nova_lista.append(lista_numero[i]) 
  nova_lista.sort()   
  return nova_lista