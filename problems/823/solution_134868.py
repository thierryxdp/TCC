def faltante(lista):
    
    i = 0 
    tamanho_lista = len(lista)
    
    while i < tamanho_lista:
        if i in not lista:
            return i
        else:
            return 0
        
        i = i +1