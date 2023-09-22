def acima_da_media(lista):

    a = sum(lista)/len(lista)
    
    for dado in lista[:]:
        
        if dado <a:
            
            lista.remove(dado)
            
    lista.sort()
    
    return lista, a