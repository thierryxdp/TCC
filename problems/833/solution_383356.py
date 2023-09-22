def conta_numero(numero, matriz):
    contador = 0

   
    for linha in matriz:
       
        for elemento in linha:
            
            if numero == elemento:
                
                contador += 1

  
    return contador