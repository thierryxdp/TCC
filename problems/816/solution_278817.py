def maiores(lista, numero):
    '''
    
    '''
   lista.append(numero)
   if max(lista) == numero:
       return []
   else:
        lista_decrescente = sorted(lista, reverse = True)
        index_n = lista_decrescente.index(numero)
        return sorted(lista_decrescente[:index_n])