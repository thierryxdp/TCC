def insere(lista_numero, n):
    #list, int -> list
    #Função que adiciona um número n dentro de uma lista de forma a 
    #deixar tal lista em ordem crescente
    
    list(lista_numero)
    lista_numero.append(n)
    lista_ordenada = sorted(lista_numero)
    
    return lista_ordenada