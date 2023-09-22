def insere(lista_numero,n):
    """Insere um número inteiro numa listra de entrada e depois ordena
    de forma crescente
    entrada=lista, int
    saída=lista
    """
  
    lista_numero=lista_numero.insert(len(lista_numero),n)    
    lista =lista_numero.sort()
    
    return lista