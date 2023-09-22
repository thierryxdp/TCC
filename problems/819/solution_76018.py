def filtraMultiplos(lista,numero):
    
    proximo = 0
    tamanho = len(lista)
    lista_f = []
    
    while proximo != tamanho:
        
        if lista[proximo] % numero == 0:
            list.append(lista_f,lista[proximo])
            
        proximo += 1
        
    return lista_f