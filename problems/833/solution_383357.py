def conta_numero(numero, matriz):
    '''Função que, dado um numero int e uma matriz de inteiros, retorna 
    quantas vezes o numero int de entrada aparece'''
    contador = 0

   
    for linha in matriz:
       
        for elemento in linha:
            
            if numero == elemento:
                
                contador += 1

  
    return contador