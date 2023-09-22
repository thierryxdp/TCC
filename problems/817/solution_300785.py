def acima_da_media(lista):
    
    for dado in lista[:]:
        
        if dado < (sum(lista)/len(lista)):
            
            lista.remove(dado)
            
    lista.sort()
    
    return lista