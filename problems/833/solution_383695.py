def conta_numero(numero,matriz):
    '''A função contará a quantidade de vezes que um (numero) aparece dentro de uma matriz
    Dados de entrada -> float,lista
    Dados de saída -> int'''
    
    nlinha = len(matriz)
   
    contador = 0
    
    if nlinha == 0:
        return 0
    else:
        ncoluna = len(matriz[0])
            
        for i in range(nlinha):
            for j in matriz[i]:
                if j == numero:
                    contador += 1

        return contador