def acima_da_media(lista_numero):

  nova_lista = []
  for i in range(len(lista_numero)):
    if lista_numero[i] > (sum(lista)/len(lista)):
      nova_lista.append(lista_numero[i]) 
  nova_lista.sort()   
  return nova_lista