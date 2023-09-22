def conta_numero(numero,matriz):
    '''
       Função que, dado um numero inteiro, retorna a quantidade
       de vezes que ele se repete numa matriz
       list,int->int
    '''
    
    final=0
    
    for i in matriz:
        for imatriz in i:
            if imatriz==numero:
                final+=1
               
   
    return final