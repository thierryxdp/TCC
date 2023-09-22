def insere(lista_numero,n): 
    "Função que dado uma lista crescente, o numero n fique em uma posição ordenada,para que a lista continue ordenada; list,int->list"
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero