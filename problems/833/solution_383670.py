def conta_numero(numero,matriz):
    '''Função que dado um número e uma lista representando
    uma matriz retorna a quantidade de vezes que esse número 
    aparece na matriz
    int,list->int'''
        
    quantidade=0
   
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j==numero:
                quantidade=quantidade+1
        
    return quantidade