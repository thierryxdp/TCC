def conta_numero(numero,matriz):
    lista=()
    
    if numero not in range(matriz):
        return 0
  
    for numero in matriz:
        lista=matriz.count(numero)
        
    return lista