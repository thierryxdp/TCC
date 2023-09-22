def insere(lista_numero,n):
    """Função na qual dada uma lista de valores ordenados e um termo inteiro n
       insere este termo na lista de forma que se mantenha ordenada."""
    #Inserindo termo na lista
    inserindo = list.insert(lista_numero,0,n)
    #Ordenando a lista novamente
    ordenando = list.sort(lista_numero)
    return lista_numero