def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros,
    a função conta e retorna quantas vezes esse numero
    aparece na matriz. int,list --> int'''
    
    
    for linha in matriz:
        for elemento in linha:
            ocorrencia=0
            
            if elemento == numero:
                ocorrencia=ocorrencia+1
                
  		return ocorrencia