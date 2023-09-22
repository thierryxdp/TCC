def repetidos(lista):
    """Função que retorna dado um lista de numeros de entrada retorna quantas vezes os numeros se repetem na lista
    list -> int"""
    vezes=0
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista[i+1:] and lista[i] in lista[i+2:]:
            vezes=vezes + 1
            
          
        
        elif lista[i] in lista[i+1:] :
            contador= contador + 1
            
    
            
        i=i+1
        
    return contador + (vezes//2)