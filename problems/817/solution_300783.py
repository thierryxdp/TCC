def acima_da_media(lista):
    
    for dado in lista[:]:
        
        if dado < 5:
            
            lista.remove(dado)
            
    lista.sort()
    
    return lista