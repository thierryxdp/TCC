def acima_da_media(lista_numero):

  nova_lista = []
  for i in range(len(lista_numero)):#percorre a lista atÃ© o final dela
    if lista_numero[i] > (sum(lista)/len(lista)):#compara o numero com a media
      nova_lista.append(lista_numero[i])#insere numero na lista 
  nova_lista.sum()#ordena a lista novamente   
  return nova_lista