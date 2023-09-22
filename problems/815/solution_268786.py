def insere(lista_numero,n):
    """ """
  
    lista_numero=lista_numero.insert(len(lista_numero),n)    
    lista= list.sorted(lista_numero)
    
    return lista