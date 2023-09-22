def insere(lista_numero,n):
    """ """
  
    lista_numero=lista_numero.insert(len(lista_numero),n)
    lista=list(lista_numero).sort(reverse=False)
    
    return lista